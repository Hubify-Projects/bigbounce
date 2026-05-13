# P4 v1.0.47 — Adversarial Cosmology-Theory Peer Review (Gemini-3.1-Pro persona)

**Reviewer persona:** Google Gemini-3.1-Pro simulating a senior cosmology theorist with a Carroll / Kamionkowski / Baumann profile — parity violation, primordial physics, EFT-of-LSS, gauge-gravity bibliography.
**Date:** 2026-05-13 10:52 PT
**Paper under review:** `pipelines/p2_chirality/chirality_catalog_paper.tex` v1.0.47 (2,732 lines, 38 bibitems).
**Charter:** find cosmology-theory defects the focused 5-agent panel missed in v1.0.46 → v1.0.47. Do NOT redundantly raise items already closed in v1.0.47 (Title/abstract reframe B1+B2, Table III ℓ-relabel B3, σ arithmetic M1, fn:mc_count M2, M_ℓℓ' narrative M4, the NEW §VIII parity-translation subsection M5 itself, Iye+2020 priority §VII.A M6, SpArcFiRe paragraph §VII.C M7, 7-region reframe M9, Shamir:2012 PLB venue M13, Shamir:2020 PASP venue M14, Holst (1995) parenthetical M15). The cosmology-translation subsection itself (§VIII.E) is **new in v1.0.47** and has not yet been adversarially audited — that is the bulk of what follows.
**Verdict TL;DR:** P4 v1.0.47 is structurally publishable, but the v1.0.47-new §VIII parity-translation subsection is the weakest part of the manuscript and contains **the most serious unresolved cosmology issue in the paper**: the morphological-dipole-to-Π translation is asserted without any derivation, the linear-response assumption is hand-waved, and the bound is quoted at the wrong order of magnitude relative to what the cited Motloch-Pen pipeline actually delivers. Either rewrite §VIII.E.(i) with a derivation chain, drop the numerical $|\Pi|\lesssim 10^{-2}$ claim, or downgrade the subsection to "qualitative complementarity" language. Two BLOCKERs, 5 MAJORs, 7 MINORs, 6 NITs.

---

## BLOCKER (2) — must address before standalone arXiv submission

### G-B1 [§VIII.E.(i), L2297–2315] — The morphological-dipole → chiral-GW Π bound is **asserted, not derived**, and the numerical value is unsupported

> "Under the standard linear-response assumption, the morphology-channel dipole bound translates to $|\Pi| \lesssim \mathcal{O}(10^{-2})$ at the horizon scale relevant for $z\!\lesssim\!1$ structure formation, weaker than (and complementary to) the CMB-birefringence bound $\beta\!=\!0.342^{\circ}\!\pm\!0.094^{\circ}$ from Eskilt~\etal~\cite{Eskilt:2023}…"

There is **no derivation chain** in the manuscript that connects the observed bound $|A_{\rm dipole}| < 5\times 10^{-3}$ (a CW-vs-CCW count fraction on a 2D projected map) to the Lue-Wang-Kamionkowski quantity $\Pi \equiv (P_L - P_R)/(P_L + P_R)$ (a tensor-power-spectrum imbalance in 3D Fourier space). The proportionality constant — call it $\alpha$, defined by $A_{\rm dipole} = \alpha \cdot \Pi$ — is not stated, motivated, or computed.

Motloch & Pen 2021 (Nature Astron. 5, 283, cited as \cite{Motloch:2021}) do NOT provide an $\alpha$. Their paper reports a correlation between galaxy spin direction and the **tidal field** reconstructed from observed galaxy positions, on a $\sim 2\times 10^5$ GZ2 sample. They do not compute a transfer function from $\Pi$ (a primordial / tensor-mode quantity in the LWK framework) onto $A_{\rm dipole}$ at $z\lesssim 1$. The transfer function is the entire content of the bound; without it, "$|\Pi| \lesssim 10^{-2}$" is a number with no provenance.

For comparison: the actual published mapping from primordial chiral GW to a galaxy-morphology observable (the closest live example is Yu et al.\ 2020 on chiral GW signatures in galaxy spins, or Biagetti & Orlando 2020 on chiral GW from inflation $\to$ LSS) goes through (a) parametrized chiral-tensor power $P_T(k)[1 + \Pi(k)\cdot \hat\sigma_3]$, (b) secondary-induced scalar parity-odd 3-point, (c) tidal-torque-theory spin alignment, (d) projection onto the chirality-asymmetry 2-point on a 2D map. Each step has an $O(1)$–$O(10^{-3})$ suppression. The end-to-end $\alpha$ in published work is typically $\sim 10^{-3}$–$10^{-1}$ with model dependence spanning $\sim 2$ orders of magnitude. The paper's $10^{-2}$ number assumes $\alpha = O(1)$, which is the most optimistic linear-response choice and is not justified.

**Why this is a blocker.** §VIII.E is sold in the title-track narrative as the bridge from morphology to the modern parity-violation parameter space. A theory referee (Carroll, Kamionkowski, Cabass, Philcox, Caldwell, or any LWK-pipeline author) will reject the subsection outright on a one-paragraph response: *"What is $\alpha$? Show the work. Cite a derivation or remove the numerical bound."* The bound is also presented as "weaker than" the Eskilt CMB-birefringence bound — but the two bounds constrain different couplings (axion-photon Chern-Simons vs.\ chiral tensor power), so the comparison itself is category-confused, not just quantitatively unsupported.

**Disposition: hard fix required.**
Three acceptable resolutions, in order of preference:
1. **Derive $\alpha$.** Write one paragraph (or one appendix) carrying out the LWK $\Pi \to$ tidal-torque $\to$ projected chirality dipole transfer-function calculation, using either the Motloch-Pen geometric kernel or an explicit toy-model linear response with stated assumptions. State $\alpha$, state the assumptions that fix it, and report $|\Pi| \lesssim (5\times 10^{-3})/\alpha$.
2. **Drop the numerical bound.** Replace "$|\Pi| \lesssim \mathcal{O}(10^{-2})$" with qualitative language: "The present dipole bound provides a model-dependent constraint on $\Pi$ whose translation requires a specific late-time projection kernel; we leave that derivation to follow-up theory work and note here only that the morphology channel is complementary to the CMB-birefringence channel as a probe of late-universe chiral tensor power."
3. **Cite an existing derivation explicitly.** If Motloch-Pen, Yu et al.\ 2020, or any published reference derives the relevant $\alpha$, cite it with equation number and reproduce the transfer-function step in one inline sentence.

Option (2) is the cheapest acceptable fix and is what I recommend for the standalone-arXiv submission. Option (1) is preferable for the eventual PRD-Letter version.

---

### G-B2 [§VIII.E.(i)+(ii), L2298–2327] — Conflation of primordial vs late-universe parity violation; no discussion of evolution, baryon-feedback, or alignment-bias systematics

The §VIII.E subsection treats the morphological chirality dipole as if it were directly constraining the **primordial** parity-violating sector (chiral tensor power $\Pi$ at horizon crossing, parity-odd trispectrum amplitude $\tau_{\rm NL}^{\rm odd}$ from inflation). It is not. The observable is a **late-universe, projected, morphology-channel** quantity at $z \lesssim 1$, sensitive to:

1. **Tidal-torque secondary effects.** Galaxy spin direction is correlated with the tidal field via TTT (Doroshkevich 1970, White 1984). Any primordial chiral signal is washed through the (parity-symmetric) tidal field of $\Lambda$CDM. The dilution factor between primordial $\Pi$ and observed spin-projected chirality is the subject of an entire literature (Catelan-Theuns 1996, Lee-Pen 2000, Yu et al.\ 2020) — none of which is cited.
2. **Baryon feedback.** Galaxy morphology (the actual observable) depends on baryonic disk formation, which is governed by gas accretion + AGN feedback + secular evolution. A chiral tensor mode at recombination can be erased by $z\lesssim 1$ baryonic processes. There is no discussion of this.
3. **Intrinsic alignment systematics.** The intrinsic-alignment literature (Joachimi et al.\ 2015, Troxel & Ishak 2015) has shown that galaxy-shape (including arm-winding) correlations with the large-scale density field have $O(1\%)$ amplitudes that are NOT primordial. These IA correlations can mimic OR mask a chirality dipole.
4. **Reading-direction / observer-frame bias.** Already addressed via TTA equivariance — but only at the classifier level, not at the alignment-bias / TTT level.

**The §VIII paragraph "(ii) Parity-odd galaxy-trispectrum amplitude" (L2316–2327)** has the same problem. The Cabass-Philcox parity-odd trispectrum is a **3-point galaxy-position observable** (parity-odd in galaxy position 4-point function — the $\zeta_4^{P\text{-odd}}$ statistic of Philcox 2022). The chirality dipole is a 2-point shape-asymmetry observable. The paper states these are "orthogonal projections of the parity-violating EFT space" — that framing is correct, but the **non-trivial question** is the cross-covariance and the relative sensitivity to a given inflationary parameter (say, the Cabass et al.\ 2023 dim-7 operator amplitude $g_*$). Neither is mentioned.

**Why this is a blocker.** A cosmology theorist will read §VIII.E and conclude that the authors do not distinguish between primordial parity violation (the language of LWK, Cabass, Philcox, Alexander-Yunes) and late-time morphological parity violation (the language of Shamir, Iye, this paper). These are different signals constrained by different observables with non-trivial overlap. The current subsection asserts they constrain "orthogonal projections" without naming the projection, without comparing sensitivities, and without acknowledging the evolution-effect / baryon-feedback / IA-bias systematics that mediate between them.

**Disposition: hard fix.** Add one paragraph after L2327 (before §VIII.E.(iii)) titled "*Late-universe to primordial: the link, and its caveats.*" Three sentences are sufficient:

> *"The chirality-dipole bound presented here is a late-universe, projected morphology-channel constraint at $z\lesssim 1$, mediated by tidal-torque theory (TTT; \cite{Doroshkevich:1970, White:1984}) and subject to baryonic-evolution and intrinsic-alignment systematics that need not be parity-violating themselves. A primordial chiral tensor signal at horizon crossing translates to the observed morphology-dipole channel with a model-dependent transfer function whose computation requires (a) tracking the chiral tensor mode through recombination and matter-radiation equality, (b) the linear-response coupling to halo angular momentum (Yu et al.\ 2020; Biagetti & Orlando 2020), and (c) the projection onto the 2D arm-winding observable conditional on the DESI Legacy footprint and depth. We do not perform this end-to-end calculation in the present paper; the bound is therefore a direct constraint on the late-universe morphology channel and only an indirect constraint on primordial parity-violating sectors. The CMB-birefringence channel (Eskilt et al.\ 2023) and the parity-odd galaxy trispectrum (Cabass et al.\ 2023, Philcox 2023) probe different observational handles on the same underlying EFT space; combining them requires the same end-to-end transfer-function calculation we defer here."*

This costs ~150 words and closes the conflation cleanly without making any claim the paper can't defend. Recommended even if G-B1 is closed via the "drop the numerical bound" route.

---

## MAJOR (5)

### G-M1 [§VIII.E.(i), L2308–2311] — The Eskilt comparison is dimensionally and physically wrong

> "weaker than (and complementary to) the CMB-birefringence bound $\beta\!=\!0.342^{\circ}\!\pm\!0.094^{\circ}$ from Eskilt~\etal~\cite{Eskilt:2023} (the latter constrains a different parity-violating coupling, the axion–photon Chern–Simons term)."

Two issues:

1. **Eskilt et al.\ 2023 is a 3.6σ measurement of $\beta$, not a bound.** Calling it "the CMB-birefringence bound $\beta = 0.342° \pm 0.094°$" is a measurement-vs-bound conflation. If the paper wants to compare bounds, the correct comparison is the 2σ upper limit, $|\beta| < 0.53°$ (or whichever side of the central value is closer to zero). If the paper wants to compare measurements, then the chirality dipole side should be reported as a measurement ($-0.122σ$, consistent with zero, with the headline upper-limit value) — which is what it already does, but the asymmetry of comparing a measured central value (Eskilt) against a bound (chirality) is misleading.

2. **"Weaker than"** is not well-defined when the two bounds constrain different couplings. $\Pi$ (chiral tensor power) and $\beta$ (axion-photon CS coupling, in degrees per Hubble-time) live in different parameter spaces with different units. The paper acknowledges this in the parenthetical ("constrains a different parity-violating coupling"), so the "weaker than" comparison should be dropped, not modified. The honest statement is *"complementary, not directly comparable"*.

**Disposition: fix.** Replace the two clauses with: "The CMB-birefringence channel \cite{Eskilt:2023} reports a $3.6\sigma$ measurement $\beta = 0.342° \pm 0.094°$ constraining a different parity-violating coupling (axion–photon Chern–Simons); the morphology channel and the CMB-birefringence channel are not directly numerically comparable and we emphasize only that the morphology channel is \emph{complementary}: a model can saturate one constraint while satisfying the other."

---

### G-M2 [§VIII.E.(iii), L2329–2348] — The ECH subsection re-introduces the "program-internal" weakness B3 was supposed to remove

The §VIII.E.(iii) ECH paragraph admits *"No published calculation provides a specific quantitative prediction for the ECH-induced chirality amplitude; the present bound is therefore a constraint on the ECH parameter space rather than a test of a falsifiable number."*

This is the same problem the Grok-4 m7 finding flagged ("§X.D bounce-cosmology section admits no quantitative ECH prediction exists. Section adds no value or weakens paper.") which v1.0.47 was supposed to address by *replacing* §X.D with the Gemini M5 parity-translation subsection. But the Holst/Mercuri/Freidel ECH paragraph survived inside the new §VIII.E as subsection (iii). The defensive disclaimer at the end ("the catalog and chirality-classification methodology presented in this paper stand on their own without dependence on any specific parity-violation theory") is a tell — the paragraph is hedging.

A hostile referee will read this as: *"The authors say they have no prediction to test, then take a paragraph to say so anyway, while linking the paper to a 4-paper program (Paper~I, II, III) — which inadvertently embeds the standalone P4 result inside the broader bounce-cosmology framing they explicitly disclaimed."*

**Disposition: drop or relegate.** Either:
1. **Delete §VIII.E.(iii) entirely.** The §VIII.E subsection becomes a cleaner two-part translation (chiral-GW $\Pi$ + parity-odd trispectrum), no ECH self-reference, no defensive paragraph. This is the cleanest standalone-arXiv option and would push readiness up another 1–2 pp.
2. **Demote to a single footnote at L2294.** *"The morphology channel also constrains the ECH parity-odd Holst sector (Holst 1995, Mercuri 2006, Freidel et al.\ 2005), though no published calculation maps the Barbero-Immirzi parameter $\gamma$ to a specific chirality-amplitude prediction; we therefore present the chiral-GW and trispectrum translations only."* This preserves the program-internal nod without giving the ECH paragraph a full subsection.

I recommend option (1) for standalone arXiv submission. Option (2) for the eventual PRD-Letter where the program-internal framing is more relevant.

---

### G-M3 [§VII.C, L1660–1668] — The SpArcFiRe monopole reconciliation is internally contradictory

> "At face value this disfavors the GZ1-attribution working hypothesis: if the GZ1 bias were the sole monopole driver, the SpArcFiRe overlap subsample should also show a CW excess (because it is drawn from the same DESI Legacy galaxy population), unless the GZ1 bias acts only through trained classifiers and not through the underlying population --- the latter is exactly what the working hypothesis says, so the SpArcFiRe non-detection of a monopole on its own (untrained) classifier is consistent with the working hypothesis rather than against it."

This paragraph **starts** by saying SpArcFiRe disfavors the GZ1-attribution working hypothesis ("At face value this disfavors…") and **ends** by saying it is consistent with the hypothesis ("…is consistent with the working hypothesis rather than against it"). The reversal happens in a single sentence pivot ("unless…the latter is exactly what the working hypothesis says").

The argument structure is: if the GZ1 bias propagates ONLY through trained classifiers and not through the underlying galaxy population, then SpArcFiRe (deterministic, not trained on GZ1) should see no monopole — which it doesn't. Therefore SpArcFiRe's non-detection is consistent.

That argument is logically valid but **rhetorically structured to confuse**. A referee will read the first clause, decide the working hypothesis fails the cross-check, and stop reading. The second clause then has to overturn the verdict — but it does so via a load-bearing assumption ("GZ1 bias acts only through trained classifiers") that is not independently motivated. In particular: if 67.6% of training labels are CE-ResNet pseudo-labels which themselves were trained on GZ1, then the "trained classifier" pathway is the dominant pathway and the assumption holds; if some fraction of the underlying galaxy population genuinely has a CW preference (e.g., from Northern-survey-direction sampling effects), then it doesn't.

**Disposition: rewrite for clarity.** Restructure the paragraph as:

> *"The published SpArcFiRe DR9-overlap catalog reports CW/CCW counts consistent with $50/50$ to within $\sim 0.3\%$ at its $\sim 1.4\times 10^5$-galaxy footprint. This is the cleanest available external probe of our working hypothesis. Under the hypothesis that the $9.5\sigma$ residual monopole originates from GZ1 human-handedness bias propagating only through trained classifiers (CE-ResNet pseudo-labels $\to$ our ViT), the SpArcFiRe deterministic algorithm — which does not use GZ1 labels in any form — should see no monopole on its overlap subsample. This is what is observed, providing consistency (not proof) of the working hypothesis. The alternative hypothesis — that the underlying DESI Legacy galaxy population has a true CW excess at the $\sim 1\%$ level for non-classifier-driven reasons — predicts a SpArcFiRe monopole at the same amplitude and is therefore not supported. A per-galaxy joint tabulation of SpArcFiRe vs.\ Catalog~C labels would tighten this test from consistency to discrimination; that tabulation is deferred to a follow-up note."*

This says the same thing without the confusing "At face value this disfavors…unless…actually it's consistent" reversal.

---

### G-M4 [Abstract L103–111, §VII.C, throughout] — The "GZ1 human-handedness bias" hypothesis lacks an independent literature anchor

The paper attributes the $9.5\sigma$ residual monopole to the *"$\sim 1\%$ human-handedness bias of the GZ1 training labels"* and cites Land et al.\ 2008 (\cite{Land:2008}). Land et al.\ 2008 (MNRAS 388, 1686) is the foundational reading-direction-bias paper that established the existence of a citizen-science handedness effect — but it reported a $\sim 5\%$ bias on the original GZ1 visual classifications, **not the $\sim 1\%$ that the present paper carries through as the working hypothesis.**

There is no citation in v1.0.47 for the specific $\sim 1\%$ number. The reader has to take the $\sim 1\%$ amplitude on the authors' word. This is fine if the $\sim 1\%$ is the post-Land-correction residual (i.e., GZ1 internally corrected the $5\%$ Land effect down to $\sim 1\%$ residual), but that pathway is not stated. Iye 2020 is cited for the reading-direction bias as well (\cite{Iye:2020}, e.g., L1538-1540), but again without a number.

**Why this matters.** The entire $9.5\sigma$ monopole interpretation rests on a quantitative match: the residual amplitude is *"consistent in magnitude with the $\sim 1\%$ human-handedness bias"* (abstract L104-106). If the actual GZ1 residual bias is $5\%$ (Land 2008 raw) or $0.3\%$ (Iye 2020 post-correction estimate), the match collapses. A referee will ask for the receipt.

**Disposition: add a sentence + footnote.** At the abstract sentence L104-106, insert: *"$\sim 1\%$ human-handedness bias of the GZ1 training labels [Land et al.\ 2008 estimated $\sim 5\%$ raw; the GZ1 release applied a correction; the residual after correction is $\sim 1\%$, as later quantified by Iye et al.\ 2020 footnote N]."* The footnote citation needs to anchor either Land 2008 §X or Iye 2020 §Y by section/eq number. Currently the $\sim 1\%$ number is a free parameter.

---

### G-M5 [Missing literature, §VIII.E and §I] — Recent (2024–2026) parity-violation literature not engaged

A cosmology-theory referee in 2026 will check whether the parity-violation literature from 2024–2026 is engaged. The current v1.0.47 §VIII.E cites:
- Lue-Wang-Kamionkowski 1999 (\cite{LueWangKamionkowski:1999}) — 27 years old, foundational
- Alexander-Yunes 2009 (\cite{Alexander:2009tp}) — 17 years old, foundational review
- Motloch & Pen 2021 (\cite{Motloch:2021}) — 5 years old
- Cabass et al.\ 2023 (\cite{Cabass:2023}) — 3 years old, foundational
- Philcox 2023 (\cite{Philcox:2023}) — 3 years old
- Eskilt et al.\ 2023 (\cite{Eskilt:2023}) — 3 years old

Notably absent (alphabetically by likely relevance):
1. **Hou, Cahn, Slepian, Cabass et al.\ (2022–2024)** parity-odd 4PCF measurements on BOSS — the empirical follow-ups to Philcox 2023. Hou, Cahn & Slepian 2023 (MNRAS or PRD; arXiv:2206.03625 family) is the second-look BOSS parity-odd analysis. Without engagement here, the paper looks frozen at 2022–2023 literature.
2. **Eskilt 2024 / Eskilt & Komatsu 2024 follow-ups.** The Eskilt et al.\ 2023 birefringence measurement has had at least one peer-reviewed follow-up in 2024 tightening the constraints and addressing the GAL040 mask systematic.
3. **Cabass, Philcox et al.\ 2024.** A follow-up paper combining the Cabass-Philcox parity-odd trispectrum framework with the empirical BOSS measurement would be natural to cite.
4. **Komatsu's 2022 review on cosmic birefringence** (arXiv:2202.13919, ARA&A 2022). The natural review citation for the §VIII.E.(i) Eskilt context.
5. **Krolewski & Ferraro 2022 / Kogai et al.\ 2018-2021** on parity-violation tests from galaxy spin alignment — direct precursors to the present paper's morphology-channel framing.

**Why this is a major.** A referee from the Carroll / Kamionkowski / Cabass / Philcox community will check the bibliography for whether the paper is engaging the live conversation in their field. Six citations to parity-violation-specific papers, with the most recent dating to early 2023, looks like the literature audit stopped at the submission start date. The standalone-arXiv version needs a 2024–2026 sweep.

**Disposition: add 3–5 citations** to §VIII.E and/or §I where the recent parity-violation literature is engaged. Minimum acceptable set: Komatsu 2022 review, Hou-Cahn-Slepian (the BOSS empirical parity-odd follow-up), Krolewski-Ferraro 2022 spin-alignment paper. This is ~30 minutes of bibitem work and meaningfully raises the cosmology-community reception readiness.

---

## MINOR (7)

### G-m1 [§VIII.E.(ii), L2316–2327] — Cabass-Philcox amplitude variable not stated correctly

The paragraph references "$\tau_{\rm NL}^{\rm odd}$ or equivalent" as the trispectrum amplitude. The Cabass et al.\ 2023 paper uses **$g_*$ (or $g_{\rm odd}$)** as the dimension-7 EFT operator amplitude that produces the parity-odd trispectrum; $\tau_{\rm NL}$ is conventionally a primordial bispectrum-amplitude variable (parity-even). The "or equivalent" hedge is doing real work here. Either:
- (a) cite the specific Cabass equation that defines the parity-odd amplitude variable used in their Fisher forecast, or
- (b) replace "$\tau_{\rm NL}^{\rm odd}$" with "$g_*$" or "the Cabass-Philcox parity-odd amplitude" and drop "or equivalent."

**Disposition: rewrite for accuracy.** Cosmetic but flagged by any referee who has read Cabass 2023.

### G-m2 [§VIII.E.(i), L2306–2308] — "Horizon scale" qualifier is ambiguous

> "the morphology-channel dipole bound translates to $|\Pi| \lesssim \mathcal{O}(10^{-2})$ at the horizon scale relevant for $z\!\lesssim\!1$ structure formation"

"The horizon scale relevant for $z\lesssim 1$ structure formation" could mean:
- (a) the comoving horizon today, $\sim 14$ Gpc;
- (b) the horizon at $z=1$, $\sim 5$ Gpc;
- (c) the comoving wavenumber corresponding to the DESI Legacy survey extent;
- (d) the wavenumber where the dipole measurement is most sensitive.

These differ by factors of $\sim 3$ in length and $\sim 10$ in wavenumber. The translation $|\Pi| \lesssim 10^{-2}$ presumably applies at one specific scale. State the wavenumber explicitly: "$|\Pi(k_*)| \lesssim 10^{-2}$ at $k_* \approx X$ Mpc$^{-1}$ corresponding to the dipole-equivalent angular scale on the DESI Legacy footprint."

**Disposition: fix or drop.** If G-B1 is closed via the "drop the numerical bound" route, this MINOR self-resolves.

### G-m3 [§I, L149–156] — The four-paper program framing inside the introduction undercuts the §I.6 "the present paper stands alone" disclaimer

> "The present chirality catalog is the morphology-channel component of a four-paper observational program; the spin-torsion no-go (Paper~I; \cite{Golden:2026P1A}), the SPHEREx $f_{\rm NL}\!=\!-35/8$ forecast (Paper~II; \cite{Golden:2026P2}), and the multi-survey 378K-anomaly catalog (Paper~III; \cite{Golden:2026P3}) cover orthogonal observational channels but the present paper stands alone --- our null dipole result does not depend on any other paper in the program."

This is a self-contradiction: paragraph 1 of the introduction frames the paper as part of a 4-paper program, then disclaims that framing in the same sentence. A standalone-arXiv reader will read the program-framing first and assume the paper is part of a coordinated submission. Either:
- (a) lead with the standalone framing and demote the 4-paper context to a final sentence of §I.6 or to the acknowledgments,
- (b) move the 4-paper framing entirely to the acknowledgments / "related work" footnote.

**Disposition: minor rewrite.** For standalone-arXiv, option (b) is cleaner. The four-paper program is a strength when submitting all four together; it is a liability when submitting P4 alone and asking the referee to evaluate the chirality null on its own merits.

### G-m4 [§VIII.E.(i), L2302–2304] — Motloch-Pen mapping is overstated

> "Tidal-torque theory (Motloch \& Pen~\cite{Motloch:2021}) maps a primordial chiral tensor sector onto a coherent galaxy-spin / arm-winding alignment via the secondary correlation with the large-scale tidal field."

Motloch & Pen 2021 do **not** map a primordial chiral tensor sector onto galaxy spins. They report an observed empirical correlation between galaxy spin and the reconstructed tidal field, with no specific mention of primordial chiral GW. Attributing the mapping to them overstates what their paper does.

**Disposition: correct attribution.** Either drop the Motloch-Pen citation here and cite Yu et al.\ 2020 (chiral GW spin alignment from inflation) or Biagetti-Orlando 2020, OR keep Motloch-Pen but rewrite: "Tidal-torque theory (\cite{Doroshkevich:1970, White:1984}; observationally verified at the $\sim 2\sigma$ level by Motloch \& Pen~\cite{Motloch:2021}) provides a kinematic correlation between galaxy spins and the large-scale tidal field; if the tidal field carries a chiral-tensor secondary, the spin direction inherits a coherent bias whose projection onto arm-winding produces the observable chirality dipole."

### G-m5 [§VII.C, L1646–1655] — "Strongest independent probe" overstates SpArcFiRe

> "SpArcFiRe is the only large-sample chirality classifier in the public literature whose handedness assignment is fully deterministic (no human-labeled training step), and is therefore the strongest independent probe of this working hypothesis available at the ${\sim}10^{5}$-galaxy scale."

This is correct as stated, but "strongest independent probe" is a bit aggressive given that (a) SpArcFiRe overlap is only $\sim 1.4\times 10^5$ galaxies vs.\ this paper's $3.2 \times 10^6$, and (b) Iye+2020 also serves as a methodological independent check at $\sim 10^5$ scale. Soften to "*the strongest fully-deterministic-classifier independent probe at the ${\sim}10^5$ scale.*" One word change.

### G-m6 [§I, L208–212] — "No evidence" still appears in the introduction body

v1.0.47's title was reframed to "A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A 0.5% Upper Limit on Large-Scale Parity Violation" per B2 — but the introduction body still says *"The result is consistent with null parity violation at the sub-percent level: no evidence for large-scale parity violation."* This is the exact language B2 was supposed to eliminate from the headline-level claims.

**Disposition: rewrite L208–212** to: *"The result is consistent with null parity violation at the sub-percent level: the equivariant CW fraction is $0.4974 \pm 0.000279$ and the dipole amplitude is bounded at $|A_{\rm dipole}| < 0.5\%$ (empirical) / $0.2\%$ (Fisher) at $3\sigma$, with the empirical bound adopted as the conservative survey-scale upper limit."* The "no evidence" framing should appear only at the level of "no evidence beyond the surveyed sensitivity," not as a categorical claim.

### G-m7 [Abstract, L94–102] — Shamir exclusion claim sigma is hand-waved

> "The $\sim\!3\%$ asymmetry reported by Shamir~(2012, 2020, 2022)~\cite{Shamir:2012,Shamir:2020,Shamir:2022} is excluded at $>5\sigma$ in the DESI Legacy footprint under the present pipeline: our maximum regional asymmetry is $\sim\!0.32\%$ (Table~\ref{tab:sky_balance}), a factor of $\sim\!6$ smaller in amplitude than Shamir's central $3\%$ claim (amplitude ratio, not significance ratio; the bracketing $\sim\!6$--$12\times$ range reflects Shamir's reported $2$--$4\%$ window)."

The "$>5\sigma$" exclusion is asserted but not arithmetically backed in the abstract. The maximum regional asymmetry $0.32\%$ vs.\ Shamir's $3\%$ is a factor of ~$10$ amplitude ratio; to convert to a significance, we need the standard error on $0.32\%$ at the regional $N \sim 6\times 10^5$ scale ($\sigma_{\rm Poisson} \approx 1/\sqrt{6\times 10^5} \approx 0.13\%$), so the regional measurement is $\sim 2.5\sigma$ from zero and $\sim 20\sigma$ from $3\%$. The "$>5\sigma$" claim is correct but the abstract should show the arithmetic in one parenthetical: "($\sigma_{\rm regional} \approx 0.13\%$, so the $3\%$ point estimate is excluded at $\sim 20\sigma$ regionally; the conservative all-sky $\geq 5\sigma$ exclusion uses the empirical $0.5\%$ MC-injection upper limit as the comparator)."

**Disposition: add the arithmetic.** ~15 words. Increases referee confidence by an order of magnitude relative to the bare "$>5\sigma$" assertion.

---

## NIT (6)

### G-n1 [§VIII.E.(i), L2298] — Citation key style inconsistency
`\cite{LueWangKamionkowski:1999}` — the multi-author camel-case key style differs from the rest of the bibliography (which uses single-first-author-only: `Cabass:2023`, `Philcox:2023`, `Eskilt:2023`). Harmonize to `Lue:1999` for stylistic consistency.

### G-n2 [§VIII.E throughout, L2288–2348] — The subsection-title "(program-internal)" qualifier in (iii) is informal
"\paragraph{(iii)~Einstein-Cartan-Holst sector (program-internal).}" — the parenthetical "(program-internal)" is informal for a published-paper paragraph header. If the subsection survives (see G-M2), drop the parenthetical and rely on the subsection content to communicate the qualifier.

### G-n3 [§I, L153] — "378K-anomaly catalog" doesn't match the Paper 3 canonical 319,443 anomaly count in CLAUDE.md
The CLAUDE.md project context lists Paper 3 at **319,443 anomalies** (matches Paper 3 Table 1 canonical 37,292,042 / 319,443). The §I.5 mention of "the multi-survey 378K-anomaly catalog" carries a stale number from an earlier Paper 3 version. Update to **319K** or **319,443**.

### G-n4 [§VIII.E.(i), L2306] — "$\mathcal{O}(10^{-2})$" notation
The order-of-magnitude bracket $\mathcal{O}(10^{-2})$ is loose for a quoted bound. A theory reader expects a specific number (e.g., $|\Pi| \lesssim 5\times 10^{-2}$ at $1\sigma$, or $|\Pi| \lesssim 10^{-1}$ at $3\sigma$). If the derivation in G-B1 is added, this resolves; if not, drop the numerical bound entirely per G-B1 option 2.

### G-n5 [§VIII.E.(ii), L2325–2327] — LSST-scale joint analysis is speculative without a forecast
> "A combined analysis using both channels on a future LSST-scale sample would tighten the joint constraint beyond what either single channel achieves."

True in the abstract sense, but stated without a Fisher forecast or any quantification. Either add "by a factor of $\sim X$ at $3\sigma$" with a number, or soften to "*could tighten*" and drop "*beyond what either single channel achieves*" (the latter is the unsupported quantitative claim).

### G-n6 [§I, L165–169] — Tadaki+2020 sample size inconsistency
> "Tadaki \textit{et~al.}~\cite{Tadaki:2020} studied a smaller sample with HSC-SSP imaging and likewise found null results."

Tadaki+2020 actually catalogs $\sim 80{,}000$ face-on spirals per its title (bibitem L2570: "*A catalogue of $\sim\!80{,}000$ face-on spirals*"). Stating "*a smaller sample*" without giving the size is fine, but the §VII.A reference to "*the third independent line of evidence consistent with the present null*" (L1597-1598) doesn't quote the size either. State once: "Tadaki et al.\ \cite{Tadaki:2020} cataloged $\sim 80{,}000$ HSC-SSP face-on spirals and likewise found null results." Cosmetic.

---

## Items NOT raised (already closed in v1.0.46→v1.0.47, do not double-up)

- B1/B2/B3 (title + abstract + Table III relabel) — closed v1.0.47.
- M1/M2/M3/M4 (σ arithmetic, fn:mc_count, Table III sig figs, M_ℓℓ' inversion) — closed v1.0.47.
- M5 (parity-translation subsection EXISTENCE) — this review audits the *content* of M5's implementation; the subsection's existence is closed.
- M6 (Iye+2020 priority engagement) — closed v1.0.47 §VII.A; content reviewed but not re-flagged at major level.
- M7 (SpArcFiRe paragraph EXISTENCE) — closed v1.0.47 §VII.C; this review audits the *internal-contradiction structure* of the paragraph (G-M3) but does not re-flag existence.
- M8/M9/M11/M12 (bias-hardening reframe, 7-region language, 0.5% empirical headline, 9.5σ monopole disclosure) — closed v1.0.47.
- M13/M14/M15 (Shamir:2012 PLB, Shamir:2020 PASP, Holst (1995) parenthetical) — closed v1.0.47.
- m1–m17, n1–n16 from the prior 5-agent panel — assumed closed and not re-audited.

---

## Total finding counts

| Severity | Count | Disposition required before standalone arXiv |
|----------|-------|----------------------------------------------|
| **BLOCKER** | **2** | Must close G-B1 + G-B2 before submission |
| **MAJOR** | **5** | G-M1 / G-M2 / G-M3 / G-M4 should close; G-M5 (literature sweep) is a 30-min bibitem pass |
| **MINOR** | **7** | Address opportunistically; G-m3 and G-m6 are cheap textual fixes |
| **NIT** | **6** | Optional; bibitem-style and language polish |
| **TOTAL** | **20** | |

## The single most concerning theory issue (one sentence)

The morphological-dipole → chiral-GW $\Pi$ translation in §VIII.E.(i) (the v1.0.47-new subsection) is asserted at the numerical level $|\Pi|\lesssim 10^{-2}$ with no derivation, no stated transfer function, no model assumptions, and a misattribution of the mapping to Motloch & Pen (who do not derive it), making the entire bound a number-with-no-provenance that any cosmology-theory referee will reject on first read — either derive the transfer function or drop the numerical bound (qualitative "complementarity" language survives the referee).

---

**Reviewer:** Gemini-3.1-Pro persona (cosmology theory / parity violation / EFT-of-LSS profile).
**Recommended next action for Houston:** address G-B1 + G-B2 (likely via Option 2 / drop-the-number routes — cheap and load-bearing-claim-preserving), close G-M1 (Eskilt comparison fix, one paragraph), close G-M3 (SpArcFiRe paragraph clarity, one paragraph), then ship v1.0.48 to standalone arXiv. Readiness P4 92 % → ~94–95 % expected on close.
