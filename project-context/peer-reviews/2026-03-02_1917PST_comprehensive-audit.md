# Comprehensive Manuscript Audit — BigBounce v0.7.0

**Date:** 2026-03-02 19:17 PST
**Reviewer:** Self-audit (skeptical physics coauthor mode)
**Manuscript version:** v0.7.0 (27 pages, commit `f009ee7`)
**PDF reviewed:** `arxiv/main.pdf` compiled 2026-03-02

---

## One-Paragraph Verdict

**Verdict: NO — not arXiv-ready today.** The manuscript has multiple *fatal* internal contradictions and missing derivations that undercut its central claims: (i) the **inflationary dilution requirement** ($N_{\rm tot}\approx92$) (Sec. II.C.2, Eq. 17-19) is incompatible with simultaneously attributing **observable** $\Omega_k\sim10^{-3}$ and $\Delta N_{\rm eff}\sim0.3$ to **bounce relics** (Sec. III.C); (ii) the dark-energy mechanism claims an operator redshifts like $a^{-3}$ yet "freezes" into $w=-1$ when its source vanishes (Sec. II.C.2), which is not derived and appears inconsistent with stress-energy logic; (iii) the **parity-odd effective action is dimensionally inconsistent as written** (Sec. II.A.2, Eq. 7 and its dimension commentary), and downstream formulas (including the abstract's $\Lambda_{\rm const}=(\alpha/M)D_{\rm inf}$) are dimensionally wrong; (iv) the CMB birefringence "prediction" lacks an explicit photon-sector coupling and relies on an undefined enhancement $f(\tau_{\rm rec})$ (Sec. III.A). On top of that, there are credibility-killing presentation errors (e.g., **Hubble tension sigma arithmetic** in Table I/Abstract vs Table III/Eq. 23), and "pitch-deck" framing ("Discovery Era," "Detection Timeline," fine-tuning bar charts) that will trigger immediate community skepticism.

---

## Top 10 Critical Issues (Severity-Ranked)

### 1) FATAL: Inflationary dilution vs bounce relic observables cannot both hold

* **What's wrong:** You require $N_{\rm tot}\approx92$ to get $D_{\rm inf}\sim10^{-121}$ (Sec. II.C.2, Eq. 17-19), but then attribute observable $\Omega_k\sim+0.001$ and $\Delta N_{\rm eff}\sim0.3$ to bounce inheritance (Sec. III.C; Table XI).
* **Why it matters:** Standard inflation makes post-bounce curvature and radiation relics essentially unobservable; your own narrative assumes standard slow-roll.
* **Where:** Sec. II.C.2 vs Sec. III.C; Eq. 17-19 vs Table XI.
* **Minimum fix:** Pick one coherent model:
  * **Option A (most salvageable):** Keep the DE dilution mechanism -> **drop** all claims that $\Omega_k$ and $\Delta N_{\rm eff}$ originate from the bounce; set them to 0 or justify them as **post-inflation** physics (but then not "bounce-predicted").
  * **Option B:** Keep bounce relics $\Omega_k, \Delta N_{\rm eff}$ -> **remove** the 92 e-fold dilution DE mechanism and replace it with a different DE derivation (major rewrite).

### 2) FATAL: Dark energy mechanism "$a^{-3}$ source" magically becomes $w=-1$

* **What's wrong:** You claim $K_{ab}\propto a^{-3}$ and $\langle K R\rangle\propto a^{-3}$ during inflation, yet also claim the residual behaves as a true cosmological constant and "freezes" when $K_{ab}\to0$ (Sec. II.C.2).
* **Why it matters:** As written, this violates basic EFT logic: if the operator expectation value is tied to a vanishing source, it should vanish unless you derive a vacuum term (VEV / effective potential / symmetry breaking / integration-out).
* **Where:** Sec. II.C.2 ("Inflationary Dilution Mechanism" + "Why $w=-1$...").
* **Minimum fix:** Either:
  * Derive an **effective constant vacuum term** in the late-time action explicitly (show the field(s) integrated out and how a constant term remains), *or*
  * Admit the DE sector is **phenomenological** (parameterize $\Lambda$ and only motivate its scale via dilution) and stop claiming a derived $w=-1$.

### 3) FATAL: Parity-odd effective action has inconsistent mass dimensions / missing prefactors

* **What's wrong:** Eq. (7) and its accompanying dimensional statement are inconsistent; later Appendix E.4 uses a different dimensional story involving an $M_{\rm Pl}^2$ prefactor. Also the Abstract defines $\Lambda_{\rm const}=(\alpha/M)D_{\rm inf}$, which is dimensionally wrong.
* **Why it matters:** If the action and operator normalization are wrong, **everything** downstream ($\Xi$, the DE scale, birefringence scaling, and any "naturalness" statements) becomes unreliable.
* **Where:** Sec. II.A.2 Eq. (6)-(8) and the text below Eq. (7); Abstract; Appendix E.4.
* **Minimum fix:** Write a single consistent EFT operator with correct dimensions (including all necessary powers of $M_{\rm Pl}$, $M$, etc.), and propagate the corrected normalization through: $\Xi$, Eq. (15)-(19), Fig. 1/5, and all claims about $\alpha/M$.

### 4) FATAL: CMB birefringence claim has no derived photon-sector coupling

* **What's wrong:** You assert your parity-odd gravitational/torsion operator rotates CMB polarization by $\beta\approx0.30°$ (Sec. III.A) but never write the EM interaction producing polarization rotation.
* **Why it matters:** Without an explicit coupling and derivation, $\beta$ is effectively a fit parameter dressed as a prediction.
* **Where:** Sec. III.A (Eq. 22 and the paragraph "From our MCMC fits...").
* **Minimum fix:** Either derive the coupling (e.g., a justified effective interaction leading to a rotation angle and its magnitude) **or delete** the claim that your mechanism predicts the measured Planck birefringence amplitude.

### 5) FATAL/MAJOR: Undefined $f(\tau_{\rm rec})$ hides enormous required enhancement

* **What's wrong:** $\beta=(\alpha/M)D_{\rm inf} f(\tau_{\rm rec})$ is asserted with $f$ undefined, yet $\beta$ is order $10^{-3}$ while your dilution parameter is order $10^{-123}$ (Sec. III.A; Sec. XII.A).
* **Why it matters:** This reads like "we need a huge factor; call it $f$." Reviewers will not accept it.
* **Where:** Sec. III.A; Sec. XII.A.
* **Minimum fix:** Derive $f$ explicitly (including its dimensions) from the actual interaction and cosmological evolution, and show it yields the right order of magnitude without absurd tuning. If you can't, remove the numerical $\beta$ claim.

### 6) MAJOR CREDIBILITY: Hubble tension significance is misstated

* **What's wrong:** Table I claims $1.4\sigma$ remaining tension (p.3), but your stated $H_0$ implies ~$2.9\sigma$ vs SH0ES (Table III).
* **Why it matters:** This looks like either sloppy arithmetic or rhetorical inflation of results; both damage trust.
* **Where:** Table I; Abstract; Conclusions repeat the "1.4sigma" line.
* **Minimum fix:** Recompute and report tensions consistently (define which dataset comparison you mean), update Table I/Abstract/Conclusions/fig captions.

### 7) MAJOR: You still overclaim "predictions" where you performed fits

* **What's wrong:** You call $H_0, \sigma_8, A_0, \beta$ "predictions/our solution," but (i) $H_0, \sigma_8$ come from Cobaya fits in an extended parameter space (Sec. VII), (ii) $A_0$ is explicitly an empirical fit parameter (Sec. II.C.3; Sec. III.B; Appendix C), and (iii) $\beta$ is claimed "from MCMC fits" (Sec. III.A).
* **Why it matters:** This triggers "model is just a re-labeled parameterization" skepticism.
* **Where:** Abstract; Table I; Sec. I.B; Sec. III; Conclusions.
* **Minimum fix:** Rewrite claims consistently: "fit," "inferred," "accommodates," "consistent with," and clearly separate what is derived vs assumed vs fit.

### 8) MAJOR: Bayes-factor presentation is inconsistent/sloppy

* **What's wrong:** Table V title ("Planck+BAO+SNIa") conflicts with Eq. (38)'s mapping of $\ln B=+4.8$ to the "Full tension" dataset; this is confusing at best.
* **Why it matters:** Evidence claims are easily attacked; if your bookkeeping is inconsistent, the whole model comparison is discounted.
* **Where:** Table V; Eq. (38); Sec. VII.C.
* **Minimum fix:** Make a single, unambiguous table listing **each dataset combination** and its $\chi^2$, AIC/BIC, and $\ln Z$; ensure labels match; explain likelihood normalizations (why Table VI $\chi^2\sim2768$ but Appendix B claims $\chi^2\sim1148$).

### 9) MAJOR: JWST JADES point on global dipole plot is misleading

* **What's wrong:** You plot a single-field raw excess alongside global dipole amplitudes (Fig. 2; Table II), even though you warn it's not comparable.
* **Why it matters:** Critics will say you're cherry-picking "supporting dots."
* **Where:** Fig. 2; Table II; Sec. III.B.
* **Minimum fix:** Remove JWST from the global dipole fit figure, or put it in a separate panel explicitly labeled "single-field raw excess (not comparable to dipole)."

### 10) MAJOR PROFESSIONALISM: "Detection timeline / Discovery era / fine-tuning scoreboards" reads like marketing

* **What's wrong:** Sections IX ("Detection Timeline"), "Discovery Era," and Fig. 5 "fine-tuning scores" + "5.9sigma by 2034" messaging.
* **Why it matters:** This triggers arXiv/community crackpot heuristics even if your math were perfect.
* **Where:** Sec. IX; Table X; Fig. 5; Table VII; Conclusions.
* **Minimum fix:** Remove timeline/era language; if you keep forecasts, put them in a restrained "Forecast" subsection with explicit assumptions and uncertainties, and do not present future "sigma milestones" as if they are scheduled.

---

## Correctness Audit (Math/Logic/Assumptions/Limits)

### A) Definitions & Dimensional Consistency

* $\Lambda_{\rm const}=(\alpha/M)D_{\rm inf}$ in the Abstract is dimensionally wrong: $\Lambda$ has dimension of mass$^2$ in the Friedmann equation, while $\alpha/M$ is stated as mass$^{-1}$ and $D_{\rm inf}$ dimensionless. You later switch to $\Lambda_{\rm eff}=\Xi M_{\rm Pl}^2+\cdots$ (Eq. 15), which is dimensionally plausible, but the paper contains both stories.
* Eq. (7) dimension narrative is inconsistent with Appendix E.4. You must choose one operator definition and track its mass dimension coherently across the paper.

### B) Logic Flow Breaks / Handwaving

* The step "$K\propto a^{-3} \Rightarrow$ diluted residual behaves as a constant vacuum energy" (Sec. II.C.2) is **not a derivation**. It's an assertion that needs an EFT argument about the **late-time effective action**.
* The galaxy spin mechanism explicitly admits the amplitude $A_0$ is not derived and is fit (Sec. II.C.3; Appendix C.3), yet the main text still markets it as a key "prediction."

### C) Limiting Cases

* Your own text says at late times the spin density is negligible and $K_{ab}\to0$ (Sec. II.C.2). In that limit, **why doesn't the parity-odd sector vanish?** You need a controlled statement: either (i) it vanishes and you don't get DE, or (ii) it has been integrated out into a constant term in the IR effective action.
* Rotation is constrained to be dynamically negligible for expansion (Sec. II.C.1), so any effect relying on the magnitude of $\omega$ should vanish. You lean on $\omega$ only for an axis, but then you must show why the axis correlates across probes if the underlying parity-odd operator is otherwise "isotropic after averaging."

### D) Stress-Energy Conservation

* If your effective energy density comes from a time-varying operator expectation value tied to spin density, you must show the associated **conservation equation** and whether energy is exchanged with matter/radiation during/after inflation. Right now it's not shown, but you still assert $w=-1$ exactly.

---

## Novelty & Positioning

### What Seems Genuinely Novel (if made consistent)

* The *attempted* UV->IR "geometric dilution" narrative linking a parity-odd Holst/EC operator to a tiny late-time vacuum scale via $e^{-3N}$ is the main distinctive angle (Sec. II.C.2; Sec. XII.A).

### What is Standard / Heavily Precedented

* EC torsion bounces / black-hole baby-universe origin are largely Poplawski's domain (refs [9-12]).
* Holst-term/Barbero-Immirzi parity physics is in Freidel/Minic/Takeuchi and Mercuri (refs [14-16]).
* $\Delta N_{\rm eff}$ and $\Omega_k$ tension games are standard parameter extensions; calling them "follow from bounce physics" without a post-inflation survival mechanism reads like relabeling.

### Overclaims to Remove

* "A Comprehensive Framework with Observational Validation" (title) is not credible given key pieces are "deferred to future work," "in preparation," and/or fit parameters.
* "End-to-end derivation ... with specific numerical outputs ($H_0, \sigma_8$)" (Sec. I.B) conflicts with your later admission that those values are fit, not derived (Sec. III.C).

---

## Observational / Validation Audit

### A) CMB Birefringence

* You cite Planck birefringence measurements and describe calibration caveats (Sec. III.A). That's fine.
* What's not fine: you assert your mechanism predicts $\beta\approx0.30°$ with no derived coupling and an undefined transfer function $f(\tau_{\rm rec})$. That is not a prediction; it's at best a post-hoc consistency statement.

**Stronger validation tests to add (if keeping birefringence):**
* Clear statement: do you actually reanalyze Planck maps, or only quote published $\beta$?
* If claiming anisotropic birefringence, specify predicted angular spectrum scaling and amplitude order-of-magnitude.

### B) Galaxy Spin Dipole

* Hierarchical Bayesian framing is the most defensible part conceptually (Sec. V; Appendix C), but lacks critical reproducibility details.
* Including JWST JADES raw excess on same plot is misleading even with caveats.

**Stronger validation tests:**
* Pre-register null tests and publish code/data splits.
* Explicitly model cosmic variance for pencil-beam fields; don't handwave "$\delta A/A\sim5-10$" without derivation.

### C) Cosmological Fits

* You add parameters $\Delta N_{\rm eff}, \Omega_k, (\omega/H)_0$ (Sec. VII.B; Eq. 37) and fit with Cobaya/CAMB modifications.
* You do not specify $\Lambda_{\rm eff}(z)$ or perturbation modifications precisely.
* Evidence accounting is messy (Table V vs Eq. 38; Appendix B vs Table VI).

**Stronger validation tests:**
* Run fits on Planck+BAO only, Planck+BAO+SN, and Planck+BAO+SN+SH0ES+DES with consistent likelihood definitions.
* Provide posterior degeneracy plots and demonstrate result is not prior-driven.

### D) Combined Significance Forecasts

* $Z_{\rm comb}$ formula (Eq. 39) cites a 1949 sociology volume (ref [37]) — bad look.
* Forecasting "5.9sigma by 2034" is not appropriate without full Fisher forecasting model.

---

## Reproducibility Checklist (What's Missing)

### Cosmology (Cobaya/CAMB)
1. Exact CAMB modification: files changed, diff/patch, explicit equations for $\Lambda_{\rm eff}(z)$.
2. Exact perturbation initial condition modifications with equations.
3. All Cobaya YAML files (priors, sampler settings, likelihood list, data version hashes).
4. Chain files (or public repository with DOI) + convergence diagnostics.
5. Table clarifying what "$\chi^2$" means for each dataset.

### Galaxy Spins
1. Catalog construction: survey IDs, query criteria, sky masks, redshift bins, all cuts.
2. CNN model card: architecture, training data, train/val/test split, augmentation, hyperparameters, calibration plots.
3. Full hierarchical model specification (priors, nuisance parameters, sampling method).
4. Code producing Fig. 2 / Table II and exact mapping from raw handedness to dipole amplitude.

### CMB EB
1. Whether EB spectra were actually computed. If yes: map products, masks, estimator, binning, validation.
2. If not: remove pipeline language and cite published results only.

---

## Revision Plan (Prioritized)

### Phase 1 — Stop the Bleeding (high impact, low conceptual risk)
1. Fix Hubble-tension arithmetic everywhere
2. Correct Table/Figure labeling inconsistencies
3. Remove or quarantine JWST JADES from global dipole plot
4. Replace ref [37] with standard statistics reference

### Phase 2 — Make Theory Internally Consistent (highest impact, required)
5. Choose inflation/bounce story (Option A recommended)
6. Repair effective action normalization with full dimensional audit
7. Fix $w=-1$ logic: derive or downgrade

### Phase 3 — Remove Unsupported "Predictions" (high impact)
8. Birefringence: derive photon coupling or remove numerical prediction
9. Stop calling fits "predictions"; reframe consistently

### Phase 4 — Reproducibility and Tone (medium/high impact)
10. Publish code/data bundle or provide permanent repository link
11. Delete Discovery Era / timeline milestones / fine-tuning scoreboards

---

## Editor Prompt (for LaTeX revision)

```
You are a skeptical physics coauthor and LaTeX editor. Your task is to produce a revised arXiv-ready manuscript from the attached draft PDF, fixing ALL issues listed below. Do not add new claims or new numerical results unless they are explicitly derived in-text. If something cannot be derived with the information we have, you must (a) remove it, or (b) downgrade it to a clearly labeled assumption/speculation.

GLOBAL RULES
1) Every equation and parameter must be dimensionally consistent.
2) Separate clearly: (i) derived results, (ii) assumptions, (iii) fitted/inferred parameters.
3) Remove marketing language and timeline "sigma milestones."
4) For every major claim, ensure the paper contains either a derivation or a precise citation.

[Full 7-step revision protocol as specified in the audit]
```

---

## arXiv Compliance Red Flags

* Title + Abstract promise too much ("comprehensive framework," "observational validation")
* "Executive summary" Table I reads like investor material
* Numerical misstatement of tension significance is the kind of thing moderators seize on
* "Reproducibility bundle is in preparation" is not reproducibility
* Notation switches between $\Lambda$, $\rho_\Lambda$, $\Xi$, and $(\alpha/M)D_{\rm inf}$ obscuring dimensions
