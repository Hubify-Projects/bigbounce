# P2 v1.7.26 — Adversarial Cosmology-Theory Peer Review (Gemini-3.1-Pro persona)

**Reviewer persona:** Google Gemini-3.1-Pro simulating a senior cosmology theorist with a Carroll / Kamionkowski / Baumann profile — primordial non-Gaussianity, EFT-of-LSS, in-in formalism, bouncing-cosmology bibliography, SPHEREx multi-tracer forecasts.
**Date:** 2026-05-13 13:30 PT
**Paper under review:** `research/focused_paper_source_integration/02_full_draft.tex` v1.7.26 (492 lines, 39 bibitems), with bib `focused_paper_refs.bib`.
**Charter:** find cosmology-theory defects beyond what R44–R51 CCAI rounds and Wave 14-PPPPP / 14-AAA closures already addressed. Do NOT redundantly raise items already closed (M2 LiBrandenberger→CaiBrandenberger rename, M3 Heinrich 2023→2024 inline, M4 Eskilt2022b, M6 Cai:2026echoes eprint, M12 Munchmeyer bibitem, M14 BF abstract specificity, B2 SDB 9.9σ demotion, B5 QSFI degenerate endpoint, B3 Cai/Li factor-of-two convention vs operator-algebra appendix, OA-B1 Dalal–Slosar 1/k² Eq. 3, OA-B4 v1.7.26-paper2 release tag).
**Verdict TL;DR:** P2 v1.7.26 is in fundamentally better shape than the chirality paper at v1.0.47 — the in-in operator-algebra appendix is genuinely well-done, the σ_theory prior-sweep ladder reads honestly, and the SDB 9.9σ demotion is the right concession. But the paper has **three latent theory issues that a hostile theorist will hit** and a set of citation gaps that, while not strictly blocking, will be flagged by any Cabass/Philcox-adjacent referee. **2 BLOCKERs, 5 MAJORs, 8 MINORs, 4 NITs.** The most concerning issue is **G-B1: the consistency-relation gauge-frame muddle** — the abstract and intro repeatedly hedge the Maldacena $|f_{\rm NL}^{\rm inf}| \approx 0.015$ value with a Pajer / Tanaka-Urakawa conformal-Fermi-frame caveat, but never tell the reader what the conformal-Fermi value actually IS, never give the suppression factor, and never reconcile this with the "×290 ratio" benchmark that drives the discrimination headline.

---

## BLOCKER (2) — must address before standalone arXiv submission

### G-B1 [Abstract, §I, §V.A] — The Maldacena-consistency-relation gauge-frame muddle: stated, hedged, but never RESOLVED

The paper invokes the Maldacena consistency relation at three load-bearing places:

- **Abstract (L29):** "$|\fnl^{\rm bounce}|/|\fnl^{\rm inf}| \approx 290$ in absolute value relative to the standard single-field inflationary gauge-frame prediction ($\fnl^{\rm inf} \approx 0.015$ at $n_s = 0.9649$, the Maldacena consistency relation)... In conformal Fermi coordinates the physical observable is parametrically smaller than the gauge-frame value~\cite{Pajer:2013,TanakaUrakawa:2011}; the bounce-vs-inflation contrast nevertheless remains $|\fnl^{\rm bounce}| \gg$ any single-field inflation observable."
- **§I (L38):** "$\fnl \approx (5/12)(1-n_s) \approx 0.015$, set by the Maldacena consistency relation~\cite{Maldacena:2002vr} (gauge-frame value; the conformal-Fermi-frame equivalent differs by $\mathcal{O}(\text{slow-roll})$ corrections~\cite{Pajer:2013,TanakaUrakawa:2011} and is not the bounce-discriminating quantity here, since the bounce-vs-inflation contrast remains $|\fnl^{\rm bounce}| \gg |\fnl^{\rm inf}|$ in either frame)."
- **§V.A (L181):** Same hedge repeated.

The structure of this hedge is theoretically incoherent in a way a competent referee will catch on first read:

1. **Pajer–Schmidt–Zaldarriaga 2013 (your `Pajer:2013` cite) is not an "$\mathcal{O}(\text{slow-roll}) correction"** to the consistency relation. Their result is that the squeezed-limit bispectrum in single-field inflation, evaluated in the **physical observer frame (conformal Fermi coordinates)**, is **identically zero** at leading order in $k_L/k_S$ — the gauge-frame Maldacena value is a coordinate artifact that is absorbed into the local definition of the background. Tanaka–Urakawa 2011 (your `TanakaUrakawa:2011` cite) makes the same point through a different gauge-transformation argument. The physical squeezed-limit consistency relation for single-field inflation in the observer frame is $\fnl^{\rm phys,sqz} = 0$, not "0.015 minus a slow-roll correction."

2. **Therefore the "×290 ratio" in the abstract is wrong as stated.** $|\fnl^{\rm bounce}|/|\fnl^{\rm inf,phys}| = \infty$, not 290. The 290 number compares the gauge-frame inflation value (a coordinate artifact) to the bounce value (which itself needs to be checked for the same coordinate artifact — see G-B2 below). This is not a small problem; it is the headline contrast the abstract sells.

3. **The "remains $|\fnl^{\rm bounce}| \gg |\fnl^{\rm inf}|$ in either frame" hedge is a non-sequitur.** In the physical observer frame, single-field $\fnl^{\rm inf,phys} = 0$ (Maldacena gauge artifact removed). The bounce prediction $\fnl^{\rm bounce} = -35/8$ is a calculation in a contracting-phase coordinate system that has NOT been audited for the same gauge artifact. Whether the gauge artifact is or is not present in the matter-bounce calculation is the **interesting physics question** of the paper; hedging past it with "either frame" boilerplate hides it.

**Why this is a blocker.** Any theorist who has read Pajer–Schmidt–Zaldarriaga or any of the post-2012 literature on the consistency-relation gauge issue (Creminelli–D'Amico–Senatore, Mirbabayi–Zaldarriaga, dePutter et al., Cabass–Pajer–Schmidt) will flag this in 30 seconds. The paper currently:
- Cites Pajer 2013 but does not state what Pajer says.
- Quotes the value 0.015 as the "standard prediction" when the consistency relation literature has spent 12 years explaining that 0.015 is NOT what any actual large-scale-structure or CMB measurement would see.
- Builds the headline discrimination on a ratio (290) that mixes a gauge-artifact numerator with an unaudited bounce-frame denominator.

The matter-bounce side may or may not survive the same gauge-artifact analysis — that is a real research question (Cabass–Schmidt 2018, Pajer 2017 review). The paper avoids it.

**Disposition: hard fix required.** Three acceptable resolutions, in order of preference:

1. **Do the audit.** Add a §V.A.1 subsection "Gauge-frame status of the bounce prediction" stating (a) the Pajer–Schmidt–Zaldarriaga / Tanaka–Urakawa physical-frame consistency relation gives $\fnl^{\rm inf, phys} = 0$; (b) the gauge transformation from comoving to conformal-Fermi coordinates contributes a piece $\propto (n_s - 1)$ that exactly cancels the Maldacena gauge-frame $5/12 (1 - n_s)$; (c) for the matter-bounce calculation, the contracting-phase mode functions are evaluated in comoving gauge and the bounce-transition gauge-fixing is implicit in the cubic-action calculation of Cai et al. (2009); (d) whether the same gauge artifact partially cancels the bounce result is an open question; (e) the contrast claim should therefore be made on observables (galaxy bispectrum amplitude, scale-dependent bias amplitude), not on $\fnl$ values across frames.

2. **Drop the ratio.** Replace "×290 ratio" with "the bounce predicts a percent-level local-shape signal where standard single-field inflation predicts a signal $\lesssim (n_s - 1) \times \mathcal{P}_\zeta \sim 10^{-9}$ at the comparable observable level (Pajer 2017 review)." This sidesteps the gauge question by quoting only what observers measure.

3. **Cite the Pajer-2017 review explicitly with the resolution.** Pajer's 2017 review (or Cabass-Schmidt 2018) provides the standard reference answer. Cite it and say: "We adopt the conventional gauge-frame Maldacena value 0.015 as the discrimination reference; observers measuring the galaxy bispectrum see the gauge-frame value because the LSS analysis pipeline does not transform to the conformal-Fermi frame. The matter-bounce contracting-phase calculation is performed in the same comoving gauge, so the contrast 0.015 vs −4.375 is the contrast in the observer-pipeline frame." This is defensible IF stated explicitly. Currently the paper neither commits to nor disclaims it.

Option (3) is the cheapest acceptable fix. Option (1) is what a refereed PRD submission requires.

---

### G-B2 [§II.A, §II.B, §II.C — the mechanism-independence claim is structurally inconsistent with §II.C's assumption (e)]

The paper repeatedly claims the $\fnl = -35/8$ prediction is **"mechanism-independent"** (§II.B title, §II.C closing, abstract, conclusion). Then in §II.C it lists five assumptions (a)–(e), where (e) is:

> "the CMB-observable modes originate from the contracting phase, not from a prolonged post-bounce inflationary epoch."

And it goes on to say:

> "Models that invoke prolonged post-bounce inflation ($N_{\rm tot} \gg 60$, as required by certain dark-energy mechanisms in modified-gravity bounce cosmologies; e.g., Cai~\&~Zhu~\cite{Cai:2026echoes}) would push the bounce-imprinted modes far beyond the observable horizon, erasing the $\fnl$ signal and replacing it with the standard slow-roll value $\fnl \approx 0.015$."

**These two claims are mutually inconsistent at the level of how a theorist reads "mechanism-independent."** The standard meaning of mechanism-independence in the bounce literature (Brandenberger 2011, Cai 2014 review, Battefeld–Peter 2014 review) is: the contraction-phase prediction is independent of the **UV completion that produces the bounce** (LQC, ekpyrotic, ghost condensate, EFT-of-bounce, etc.). It does NOT mean the prediction is independent of whether there is a post-bounce inflationary attractor — those are two different sectors of bounce-model space.

The paper conflates these. The phrasing "mechanism-independent in the sense that it depends only on the contracting-phase dynamics, not on the specific UV completion that produces the bounce" (§II.B) is correct as defined; but then the abstract sells the prediction as **"$\fnl^{\rm local} = -35/8$ (Cai et al. 2009)"** as if it were universal across the matter-bounce class, when it is actually restricted to bounce models that (e) do not have a prolonged post-bounce inflationary epoch.

This is not academic. The dominant bounce-models-with-dark-energy class — the very class that Houston's research program (per `project-context/bounce_portfolio_strategy.md`) keeps open as alternatives — includes models like Cai–Zhu 2026 (your own cite `Cai:2026echoes`) where post-bounce slow-roll IS invoked to generate the late-time accelerating phase. The paper's prediction does not apply to those models, but the abstract does not say so.

**Why this is a blocker.** A theorist asked to assess the breadth of the matter-bounce prediction will conclude: "the prediction applies to the Wilson-Ewing model (only), is named 'matter bounce' as if generic, and the post-bounce-inflation assumption that restricts it to ~one model is buried in §II.C assumption (e) without being signaled in the abstract." The paper-level falsification claim ("SPHEREx null would disfavor the quasi-dust matter bounce benchmark at $>4\sigma$ under assumptions (a)–(e)") is technically defensible but is sold with much more breadth than the assumption set supports.

**Disposition: hard fix.** Either:

1. **Narrow the abstract claim.** Replace "$\fnl^{\rm local} = -35/8$ (Cai et al. 2009)" in the first sentence with "$\fnl^{\rm local} = -35/8$ (Cai et al. 2009) **in matter-bounce models without prolonged post-bounce inflation** (the Wilson-Ewing class; bounce models with $N_{\rm post-bounce} \gg 60$ inflate the signal beyond the observable horizon)." One clause, no significance lost.

2. **Drop "mechanism-independent" from the title-track language.** Replace with "model-class-specific" or "quasi-dust-contraction-specific." The paper would then be honest about the scope: it is a test of one bounce subclass, not the bounce paradigm. A null result would falsify Wilson-Ewing, not the broader bounce program.

3. **Or, less preferred: state both.** Keep "mechanism-independent" as the UV-completion claim, but add one sentence to the abstract: "This prediction applies to bounce models without prolonged post-bounce inflation (the Wilson-Ewing class); bounce models with significant post-bounce inflationary expansion fall outside this benchmark."

Option (1) is the cheapest path. The Wilson-Ewing narrowing is already in the paper at §II.D — it just needs to be hoisted to the abstract.

---

## MAJOR (5)

### G-M1 [§VIII.D, L369] — QSFI shape formula is correct but the Higuchi-bound statement is sloppy

The paper writes the QSFI squeezed-limit shape (§VIII.D, ref `Chen:2009zp`):

$$ \Delta = 3/2 - \sqrt{9/4 - \mu^2/H^2} $$

with the limiting cases "At $\mu/H = 0$ (massless heavy field) $\Delta = 0$" and "at $\mu/H = 3/2$ (Higuchi-bound limit) $\Delta = 3/2$."

**The Higuchi-bound attribution is wrong.** The Higuchi bound applies to **massive spin-2** fields in de Sitter, $m^2 \geq 2H^2$ — a different bound, on a different field species. The QSFI scenario of Chen–Wang 2009 uses a **massive scalar** with mass $\mu$; the relevant bound on the squeezed-limit power is the **complementary-vs-principal series transition** at $\mu/H = 3/2$ (the unitarity boundary of the scalar representation of the de Sitter group, sometimes called the "principal-series threshold" or just "$m = 3H/2$ transition"), not the Higuchi bound.

A senior theorist (Arkani-Hamed–Maldacena 2015 "Cosmological Collider Physics" is the canonical pedagogical reference here) will flag the misattribution immediately. The physics statement — that $\mu/H = 3/2$ is the boundary at which the squeezed enhancement of the bispectrum saturates the local-template scaling — is correct; only the name is wrong.

**Disposition.** Replace "Higuchi-bound limit" with "principal-series boundary" or "$m=3H/2$ unitarity boundary" (whichever the author prefers). Optionally add a cite to Arkani-Hamed–Maldacena 2015 (arXiv:1503.08043) for the standard treatment. One word fix.

### G-M2 [Abstract, §VI conclusion, §VIII.A] — PBH abundance and induced-GW connections from $f_{\rm NL} = -4.375$ are completely missing

The abstract and conclusion sell the matter-bounce $f_{\rm NL} = -4.375$ prediction as a test of bouncing cosmology vs inflation. They do not mention that this same parameter has two other observational consequences that any modern (2022–2026) NG paper is expected to cover:

1. **Primordial black hole abundance.** A negative $f_{\rm NL}$ at this magnitude suppresses the tail of the curvature-perturbation PDF, modifying the PBH formation threshold via the Edgeworth expansion correction to Press-Schechter (Franciolini–Iovino–Vaskonen–Veermäe 2022, Young–Byrnes 2013). For $f_{\rm NL} = -4.375$ the PBH suppression factor is $\mathcal{O}(0.1)$ relative to the Gaussian case at the formation scale, which is a real observational consequence and is independently testable via LIGO–Virgo–KAGRA mass-distribution fits, PBH-DM bounds, and OGLE microlensing. CLAUDE.md states this is already a result of Houston's broader program ("PBH abundance from f_NL=-4.375: Edgeworth expansion correction to Press-Schechter"). It belongs in the discussion.

2. **Scalar-induced gravitational waves.** Negative $f_{\rm NL}$ at this level modifies the second-order tensor power generated from the scalar bispectrum, predicting a specific spectral index $\gamma_{\rm GW} \approx 3.0$ at the NANOGrav 15yr band. This is the Paper 3 PTA connection (per CLAUDE.md "Combined PTA GPU MCMC: γ = 3.20 ± 0.42 (Paper 3 §6 canonical), bounce γ=3.0 at 0.48σ"). The cross-paper coupling is one of the strongest pieces of multi-messenger physics in the broader program and is **not cited anywhere in Paper 2**.

**Why this is a major.** The paper currently sells $f_{\rm NL} = -4.375$ as a one-channel prediction (galaxy bispectrum / SDB) when it is in fact a three-channel prediction (bispectrum + PBH + induced GW spectral shape). Reviewers will ask: "Why is the PBH and SI-GW physics not in this paper?" The answer "it is in companion papers" is fine IF the cross-references are explicit. They are not.

The SSOT for P2 (§6 "Cross-paper dependencies") notes "Paper 2 ↔ Paper 3: Paper 2 discusses 'improved tracer sample' in §4/§5 without explicit citation to Paper 3" and resolved this as "no cross-ref needed." That resolution is wrong now: the cross-ref is needed not for the tracer sample, but for the $f_{\rm NL} \to \gamma_{\rm GW}$ coupling.

**Disposition.** Add 2–3 sentences to §VIII.A or a new §VIII.F:

> "The matter-bounce $f_{\rm NL} = -4.375$ prediction has two further observational consequences beyond the galaxy bispectrum channel forecast here. First, the negative skewness of the primordial curvature distribution modifies the high-$\zeta$ tail relevant for primordial black hole formation through the Edgeworth correction to Press-Schechter (Franciolini et al.\ 2022, Young \& Byrnes 2013), suppressing the PBH abundance by $\mathcal{O}(0.1)$ at the formation scale and producing a complementary handle from LIGO–Virgo–KAGRA mass-distribution fits. Second, at second order the scalar bispectrum sources induced gravitational waves with a spectral index $\gamma_{\rm GW} \approx 3.0$ at the NANOGrav 15yr band; the companion analysis of \cite{Golden:2026anomaly} compares this prediction against the observed $\gamma = 3.20 \pm 0.42$ at $0.48\sigma$ consistency. The bispectrum-channel SPHEREx forecast presented here is therefore one of three independent observational tests of the same minimally parameterized prediction."

Three new cites (Franciolini 2022, Young-Byrnes 2013, Golden:2026anomaly). One paragraph. Reviewers will read this as the paper closing a real cross-paper coupling rather than leaving it as a loose end.

### G-M3 [§II — quasi-dust assumption $n_s = 1$ vs observed $n_s = 0.9649$ is undersold as a limitation]

The matter-bounce contracting-phase prediction at $w = 0$ exactly gives $n_s = 1$ (scale-invariant scalar power). The observed Planck value is $n_s = 0.9649 \pm 0.0042$, which is $> 8\sigma$ from unity. The Wilson-Ewing escape is to invoke $w = -0.003$ (quasi-dust), giving $n_s = 1 + 12 w = 0.964$.

The paper handles this at §II.D:

> "$n_s = 0.964$ (from $w = -0.003$, one free parameter tuned to the Planck observed $n_s = 0.9649 \pm 0.0042$; the spectral index formula $n_s = 1 + 12w$ follows from the growing-mode solution in quasi-dust contraction)"

**The problem:** the paper calls this "one free parameter tuned to the data" in passing, but does not honestly stage the **structural cost**. Standard slow-roll inflation makes $n_s \neq 1$ a **prediction** of the slow-roll dynamics (departure from de Sitter); the matter bounce makes $n_s \neq 1$ a **tuning** of an EOS parameter that has no UV-completion motivation in the bounce sector. This is a real asymmetry that the §V.B "kinematic vs parametric" subsection (L194) does not acknowledge — that subsection lists the bounce as "kinematic" (good) and inflation as "parametric" (bad), but $n_s$ alone reverses this scoring: inflation is kinematic in $n_s$, the bounce is parametric in $n_s$.

A senior theorist reading §V.B will say: the kinematic-vs-parametric framing cherry-picks $f_{\rm NL}$ and ignores $n_s$. A complete framing notes that:
- In $f_{\rm NL}$: bounce is kinematic, inflation is parametric → bounce wins.
- In $n_s$: bounce is parametric (tuned $w$), inflation is kinematic (slow-roll) → inflation wins.
- Net: the kinematic-vs-parametric scoring is a wash, and the Bayesian preference rests on the actual numerical comparison, not on the framing.

**Why this is a major.** §V.B is one of the most rhetorical sections of the paper and is the framing the abstract sells ("kinematically determined ... parametrically accommodate"). It will not survive a hostile theory referee unchanged.

**Disposition.** Either:

1. **Rewrite §V.B to acknowledge the symmetry.** Two sentences added after "drives a natural Bayesian preference for the bounce":

> "We note that the kinematic-vs-parametric scoring depends on which observable is being compared. The matter-bounce $n_s$ requires a tuning of the contraction-phase equation of state ($w = -0.003$) that is itself parametric, whereas slow-roll inflation makes $n_s \neq 1$ a kinematic consequence of the slow-roll dynamics. The Bayesian preference favoring the bounce is therefore driven by the $f_{\rm NL}$ contrast, not by a generic 'kinematic beats parametric' asymmetry. The Wilson-Ewing $f_{\rm NL}$-$n_s$ consistency relation (§VII.B) partially mitigates this by tying both observables to the single parameter $\epsilon$, but the residual $w \to 0$ tuning remains."

2. **Or, weaker: at least cite $n_s$ as a separate competitor handle.** One sentence: "We note separately that the spectral index $n_s = 0.9649$ is a slow-roll prediction in inflation and a tuned parameter in the matter bounce; the kinematic-vs-parametric framing of this subsection refers specifically to $f_{\rm NL}$."

Option (1) is the principled fix.

### G-M4 [§VIII.A — `Eskilt:2023` cite key inconsistency with bib `Eskilt2022b`]

The R51 CCAI review confirmed `Eskilt2022` and `Eskilt2022b` coexist correctly in the bib, with `Eskilt2022b` being the Cosmoglobe DR1 ApJ entry. Spot-checking line 379, the text reads:

> "the $3.6\sigma$ Eskilt \etal~\cite{Eskilt2022} joint Planck analysis and the $2.9\sigma$ ACT~DR6 measurement of Diego-Palazuelos \etal~\cite{DiegoPalazuelos2025} are both consistent with the bounce ALP prediction. Quantitatively, the bounce prediction $\beta = 0.27^\circ$ is consistent with the published Cosmoglobe DR1 Planck+ACT joint measurement of Eskilt \etal~\cite{Eskilt2022b} $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$..."

**Inconsistency:** the $3.6\sigma$ Planck-only Eskilt result cited as `Eskilt2022` ($\beta = 0.30^\circ \pm 0.11^\circ$ on Planck PR4) and the Cosmoglobe DR1 Planck+ACT joint result cited as `Eskilt2022b` ($\beta = 0.342^\circ \pm 0.094^\circ$) are both attributed to "Eskilt et al." — which they are, but with different first-author leads in some of the joint-author lists. More importantly, **the $0.342^\circ \pm 0.094^\circ$ measurement is from a DIFFERENT paper from the $0.30^\circ \pm 0.11^\circ$ result**, and the reader cannot tell from the prose which $\sigma$ figure belongs to which.

The $3.6\sigma$ figure attributed to `Eskilt2022` is from Eskilt 2022 Planck-only; the $\beta_{\rm obs} = 0.342^\circ$ cited as `Eskilt2022b` is from Eskilt et al. 2023 Cosmoglobe DR1 ApJ. CLAUDE.md confirms: **"ALP birefringence prediction β = 0.27° matches 3.6σ observed signal (0.342 ± 0.094°)"** — so CLAUDE.md attributes the $0.342 \pm 0.094$ to the $3.6\sigma$ result, but the paper attributes the $3.6\sigma$ to a different cite key.

This is a citation-vs-prose mismatch that a referee will ask about. Either:
- The $3.6\sigma$ figure is the Cosmoglobe DR1 result, in which case the cite at L379 line 1 should be `Eskilt2022b` not `Eskilt2022`.
- The $3.6\sigma$ is the Planck-only result and the Cosmoglobe joint is a separate (compatible) measurement, in which case the prose should distinguish them explicitly.

**Disposition.** Rewrite the L379 sentence chain to make it unambiguous which $\sigma$ belongs to which cite key, and reconcile with CLAUDE.md. Suggested:

> "The Cosmoglobe DR1 joint Planck+ACT analysis of Eskilt \etal~\cite{Eskilt2022b} reports $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$, a $3.6\sigma$ deviation from zero; the earlier Planck-only analysis of Eskilt \etal~\cite{Eskilt2022} gave a consistent but lower-significance $\beta = 0.30^\circ \pm 0.11^\circ$ ($2.7\sigma$). The independent ACT DR6 measurement of Diego-Palazuelos \etal~\cite{DiegoPalazuelos2025} ($2.9\sigma$) is consistent with both. The bounce prediction $\beta = 0.27^\circ$ sits at $0.77\sigma$ from the Cosmoglobe DR1 central value and well within the $1\sigma$ joint uncertainty."

### G-M5 [§VIII.A — birefringence subsection is "bounce-motivated" but the ALP coupling is never specified at the parameter level]

§VIII.A (L379) introduces cosmic birefringence as "a complementary test of bounce-motivated physics" and states:

> "the prediction $\beta\approx 0.27^\circ$ depending on the ALP coupling $g_{\phi\gamma}$ and ALP mass $m_a$ being consistent with sub-eV/super-Planck-coupled spectator-ALP windows (so the test is bounce-motivated rather than parameter-free in the Maldacena-consistency-relation sense)"

**This is a hand-wave.** The ALP-birefringence prediction $\beta \propto g_{\phi\gamma} \cdot \phi_0$ depends on **two** parameters: the photon-ALP coupling $g_{\phi\gamma}$ and the field excursion $\phi_0$ (set by the ALP mass and initial misalignment). The paper says these are "consistent with sub-eV/super-Planck-coupled spectator-ALP windows" but does not give any numerical values, does not state the equation $\beta = (g_{\phi\gamma} \phi_0 / 2)$ or its more careful form, and does not say what the specific bounce-prediction for $g_{\phi\gamma}$ or $\phi_0$ is.

A hostile referee will note: the headline claim of the abstract is that the matter-bounce $f_{\rm NL}$ prediction is "minimally parameterized" — but the birefringence cross-link in §VIII.A is dragged in to support the bounce paradigm and is **not** minimally parameterized (it has two free parameters). The birefringence claim therefore weakens the paper's framing rather than strengthening it.

**Disposition.** Either:
1. **Cut §VIII.A.** The bounce-birefringence connection is a side claim that doesn't drive any forecast in this paper; cutting two paragraphs costs nothing.
2. **Strengthen §VIII.A.** State the $g_{\phi\gamma} \phi_0 = 2\beta$ relation, quote a specific allowed window, and cite the bounce-ALP coupling paper that derives it (Paper 1? If so, cross-cite).
3. **Reframe §VIII.A as "weak cross-check, not falsification."** One sentence: "We note in passing that the same bouncing-cosmology framework can host a cosmic-birefringence signal at the $0.27^\circ$ level (see companion paper \cite{Golden:2026framework}); this is a separate observable with a separate parameter budget and does not drive the forecasts of the present paper."

Option (3) is cheapest. Option (2) is best for the long-term program.

---

## MINOR (8)

### G-m1 [§V.B `Cai:2018non` cite — wrong-sign non-attractor inflation $\fnl = +5/2$ claim]

§V.B states "Non-attractor single-field inflation naturally gives $\fnl = +5/2$ (wrong sign)~\cite{Cai:2018non}." The standard non-attractor result (Namjoo–Firouzjahi–Sasaki 2013, Chen et al.\ 2013, Mooij–Palma 2015) is $\fnl = 5/2$ in **specific** non-attractor regimes (ultra-slow-roll with constant Hubble), but the sign and value are scheme-dependent depending on whether one quotes the squeezed-limit or the equilateral-limit value. The "+5/2 (wrong sign)" claim should cite the canonical Namjoo–Firouzjahi–Sasaki 2013 (arXiv:1210.3692) result rather than the `Cai:2018non` entry (which is one of many follow-ups). Recommend adding the NFS 2013 cite or replacing `Cai:2018non` with it.

### G-m2 [§VIII.D — missing cite for Suyama-Yamaguchi inequality]

L371: "$\tau_{\rm NL} \geq (6\fnl/5)^2$" is cited as a "single-source consistency relation" with no bibitem for the actual Suyama-Yamaguchi paper (arXiv:0709.2545, PRD 77, 023505). This is the canonical reference; not citing it is a citation hygiene flag. Add `Suyama:2007bg` to the bib.

### G-m3 [§II.A — Wilson-Ewing $n_s = 1 + 12w$ derivation is not standard textbook]

§II.A and §VII.B both invoke $n_s = 1 + 12w$ as the matter-bounce spectral-index formula, citing `WilsonEwing:2012`. The standard derivation (Wands 1999, Finelli-Brandenberger 2002) gives $n_s = 1 + 2(3w - 1)/(3w + 1)$ in the general $w$-bounce case, which reduces to $n_s = 1$ at $w = 0$ and gives a different first-derivative coefficient than 12 at the matter-domination point. The factor of 12 in $n_s = 1 + 12w$ is correct in the limit $w \to 0$ where the formula linearizes, but the paper should cite the Wands/Finelli-Brandenberger derivation explicitly and note this is the linearized form. One sentence + cite.

### G-m4 [§V.B "minimum curvaton $f_{\rm NL} \approx -1.25$ insufficient" — undercited]

L183: "The standard quadratic curvaton gives minimum $\fnl \approx -1.25$ (insufficient)." This number traces back to Sasaki–Valiviita–Wands 2006 (arXiv:astro-ph/0607627) and was reviewed in Wands 2008. The paper does not cite either. Add `SasakiValiviitaWands:2006` to the bib for the curvaton-class lower bound.

### G-m5 [§VIII.D `n_{\rm NL}` running attribution]

L369: the "$n_{\rm NL} \equiv d\ln|\fnl|/d\ln k$ running parameter" is introduced without a citation to the source of the parameterization. The standard reference is Chen 2005 (arXiv:astro-ph/0507053) or Byrnes-Choi-Hall 2010 (arXiv:1007.1245). Add one.

### G-m6 [Bib `Heinrich:2023` handle vs 2024 inline year stamp]

The R51 review confirmed the handle is intentionally `Heinrich:2023` (preprint year) while the inline year stamp is now 2024 (published year). This is defensible but unconventional — most arXiv-style bib management uses the published-year handle. Recommend renaming the handle to `Heinrich:2024` for consistency. Cosmetic, but a referee may flag it.

### G-m7 [§II.A Cai:2009 polynomial coefficient footnote — sign of $c_3$ inconsistency]

L70 footnote: "The coefficients printed in Eq.~(37) of~\cite{Cai:2009fn}---$(3, 1, -9, 5, -66, 9)$---are the single-time-ordering values (before the in-in commutator doubling). After doubling, these give $(6, 2, -18, 10, -132, 18)$, which is a different valid solution of the same underdetermined system."

Sign check: $(3, 1, -9, 5, -66, 9) \times 2 = (6, 2, -18, 10, -132, 18)$. Correct. But the **reference coefficient set used in the computational analysis** is $(2, 7, 3, -12, -69, 19)$ (L70), which is NOT $2\times$ the Cai single-ordering coefficients $(3, 1, -9, 5, -66, 9)$, nor is it the doubled set $(6, 2, -18, 10, -132, 18)$. The paper says this is a different valid null-space solution; that's defensible mathematically, but the prose should explicitly say "We chose a different null-space representative for numerical-stability reasons; this is one of infinitely many valid coefficient sets that satisfy the three benchmark constraints." Currently the relationship between $(2, 7, 3, -12, -69, 19)$ and the Cai-published coefficients is not stated, only the relationship between Cai's two coefficient sets.

### G-m8 [§IV `\sim 10$--$20\%$ improvement` from anomaly tracers is hand-waved]

§IV (L156) claims: "a preliminary Fisher forecast on DESI–SDSS cross-matched anomaly tracers projects a ${\sim}\,10$--$20\%$ improvement in $\sigma(\fnl)$ over the standard multi-tracer baseline." The "preliminary Fisher forecast" is not cited (Paper 3?), not quantified beyond the percentage range, and the shot-noise caveat is acknowledged in the next paragraph but not resolved. The 10–20% number reads as a placeholder. Either cite Paper 3 explicitly with the supporting calculation, or remove the number and replace with "a potential improvement of order $\sim$10–20% pending shot-noise-corrected forecast (companion analysis)."

---

## NIT (4)

### G-n1 [Bib `Munchmeyer:2019` — Münchmeyer not Munchmeyer]

The bibitem renders the umlaut correctly via `M\"unchmeyer` in the .bib but the cite handle is `Munchmeyer:2019` without the umlaut. Cosmetic; not a defect. Cross-checked at R51 as clean.

### G-n2 [Abstract sentence length]

The abstract is a single sentence of ~750 words and ~50 inline LaTeX expressions. PRD abstracts are formally allowed to be one paragraph, but ~750 words tests reader endurance. A judicious paragraph break after "validated via $\ell$-space Fisher overlap, 200 injection-recovery realizations, and a $10{,}000$-sample null-space scan of the underdetermined polynomial coefficients (shape cosine $r_{\cos} > 0.97$ for all samples)." would help.

### G-n3 [`\textit{et~al.}` macro and `Cai \textit{et~al.}` rendering]

The `\etal` macro is defined as `\textit{et~al.}` (line 13). Some inline uses use `\etal` (e.g., L29 "Heinrich \etal~2024"); others spell out `Cai \textit{et~al.}` directly (e.g., L34 "Cai \textit{et~al.}~\cite{Cai:2009fn}"). Pick one for the final manuscript pass.

### G-n4 [§VII.B `$c \in [-0.7, -10]$` — order convention]

L329: "$c \in [-0.7,\;-10]$." Conventionally, intervals are written with the smaller (more negative) number first: $[-10, -0.7]$. Cosmetic.

---

## Recommended next action

This is a 99%-cap paper. None of the items above are fatal, but G-B1 (consistency-relation gauge-frame muddle) and G-B2 (mechanism-independence vs. assumption (e) inconsistency) are the kind of issues a competent theory referee will hit on first read. Both have cheap acceptable resolutions (one paragraph each). The cheapest end-to-end pass that addresses all BLOCKERs and MAJORs is roughly:

- **G-B1 fix (option 3):** ~1 paragraph in §V.A acknowledging the Pajer-Schmidt-Zaldarriaga / Tanaka-Urakawa gauge issue and committing to observer-pipeline-frame contrast. Cite Pajer 2017 review or Cabass-Schmidt 2018.
- **G-B2 fix (option 1):** Hoist the Wilson-Ewing narrowing to the abstract as one clause.
- **G-M1 fix:** One-word change (Higuchi-bound → principal-series boundary).
- **G-M2 fix:** One new paragraph + 3 new cites (Franciolini, Young-Byrnes, Golden:2026anomaly).
- **G-M3 fix:** Two sentences in §V.B acknowledging the $n_s$-side parametric cost.
- **G-M4 fix:** Rewrite one sentence in §VIII.A to disambiguate the Eskilt cites.
- **G-M5 fix (option 3):** Reframe §VIII.A as "weak cross-check, not falsification" in one sentence.

Total wall-clock: ~2–3 hours of focused writing. PDF recompile per the PDF-recompile-protocol (bundled .tex version/date bump → recompile → mirror to 5 surfaces → SSOT update in same commit).

The paper is closer to clean than v1.0.47 of the chirality paper was. The two BLOCKERs are real but cheap to close, and the MAJOR/MINOR list is the kind of thing a competent rebuttal letter handles in a 2–3 page response.

---

## Counts

- **BLOCKERs:** 2 (G-B1 gauge-frame muddle, G-B2 mechanism-independence vs. assumption (e))
- **MAJORs:** 5 (G-M1 Higuchi-bound misattribution, G-M2 PBH+SI-GW cross-paper cite missing, G-M3 $n_s$-side parametric-cost asymmetry, G-M4 Eskilt cite-vs-prose mismatch, G-M5 birefringence parameter hand-wave)
- **MINORs:** 8 (G-m1 through G-m8)
- **NITs:** 4 (G-n1 through G-n4)
- **Total open items:** 19

**Most concerning theory issue:** G-B1 — the consistency-relation gauge-frame muddle. The paper cites Pajer 2013 and Tanaka-Urakawa 2011 (which together establish that the single-field physical observer-frame consistency relation gives $f_{\rm NL}^{\rm inf, phys} = 0$, not 0.015) but then quotes the gauge-frame Maldacena value 0.015 as the "standard prediction" and builds the headline ×290 ratio on it. A senior theorist will flag this immediately. The fix is one paragraph committing the paper to an observer-pipeline-frame contrast statement, which is defensible and standard practice — but currently the paper hedges past it.
