# Claims Table: Derived vs Assumed vs Fit/Inferred

**Date:** 2026-03-02 19:17 PST
**Manuscript version:** v0.7.0

This table classifies every headline result in the manuscript. The editor target is to make the post-revision paper accurately label each item.

---

## A) Theory Core (Action, Operators, Conventions)

| Item | Current Claim | Status | Where | Editor Target |
|------|---------------|--------|-------|---------------|
| Einstein-Cartan-Holst + torsion-squared baseline action $S_{ECH}$ | Defines starting action with Holst term and torsion term | **Assumed (model definition)** | Eq. (1) | Fine as definition; align conventions with appendices |
| $\gamma = 0.274\pm0.020$ "fixed by LQG" | Uses LQG entropy counting to "fix" $\gamma$ | **Assumed w/ citation** | Eq. (2) | OK as external input |
| Torsion algebraic: $T_{abc}=8\pi G S_{abc}$ | Torsion is nondynamical and algebraically determined | **Derived/standard (incomplete writeup)** | Eq. (3) + Step 1 | Needs consistency with later $DK$ terms in $S_{\rm eff}$ |
| Four-fermion interaction after integrating torsion | $L_{\rm int}\propto J_A^\mu J_{A\mu}$ with $\gamma^2/(\gamma^2+1)$ factor | **Derived/standard (citation-level)** | Eq. (4) | Treat as standard result, cite carefully |
| Parity-odd effective action $S_{\rm eff}$ exists | $S_{\rm eff} = (\alpha/M)\int e\wedge e\wedge F[K,\mathring R]$ | **Assumed / motivated (not derived)** | Eq. (6)-(8) | Keep as phenomenological EFT |
| "Dimensionally consistent" claim for Eq. (7) | Tetrad-curvature combo has mass dimension 5 | **Incorrect / needs repair** | Eq. (7) text | Conflicts with Appendix E.4 |
| "Parity-odd sector carries $\alpha/M$ independently" | Claims EH prefactor separate | **Assumed (conflicts later)** | After Eq. (7) | Reconcile with Appendix E.4 |
| "Torsion remains algebraic" even with $DK$ | Correction is $O(\alpha/(M M_{\rm Pl}^2))\sim10^{-3}$ | **Assumed / not properly dimensioned** | After Eq. (7) | Needs real scale analysis |
| One-loop estimate for $\alpha/M$ | Scheme-dependent; treats $\alpha/M$ phenomenologically | **Assumed + qualitative motivation** | Eq. (8)-(9); Sec. IV.A | Appropriately cautious in Sec. IV.A; match in abstract/title |

---

## B) Dark Energy Mechanism

| Item | Current Claim | Status | Where | Editor Target |
|------|---------------|--------|-------|---------------|
| $\Lambda_{\rm eff} = \Lambda_{\rm const} + c_\omega\omega^2$ | Defines late-time $\Lambda_{\rm eff}$ with rotation term | **Assumed (model choice)** | Abstract; Eq. (14) | $c_\omega=-1$ claimed but not shown in main text |
| $\Lambda_{\rm const}=(\alpha/M)D_{\rm inf}$ | Stated directly | **Incorrect dimensionally** | Abstract; Sec. I.B | Must be fixed or removed |
| $\Xi \equiv [(\alpha/M)M_{\rm Pl}]D_{\rm inf}$ and $\rho_\Lambda = \Xi M_{\rm Pl}^4$ | Defines geometric dilution parameter | **Assumed (definition) + partially derived scaling** | Eq. (15)-(16); Eq. (40) | Core claim; dimension-check consistently |
| Inflationary dilution $D_{\rm inf}=e^{-3N_{\rm tot}}(T_{\rm reh}/M_{\rm GUT})^{3/2}$ | Key scaling | **Assumed / heuristic** | Eq. (17) | Needs derivation of why exponent is exactly 3 |
| Requires $N_{\rm tot}\approx92$ to match $\rho_\Lambda$ | Computes $D_{\rm inf}\sim10^{-121}$ | **Derived from assumed formula** | Sec. II.C.2 | Inference from scaling assumption, not prediction |
| "Why $w=-1$" + "$K_{ab}\to0$ but residual freezes" | Claims true CC emerges | **Not derived / logically inconsistent** | Sec. II.C.2 | Central fix: derive IR constant term or downgrade |

---

## C) Rotation / Axis / Anisotropy

| Item | Current Claim | Status | Where | Editor Target |
|------|---------------|--------|-------|---------------|
| Rotation negligible for expansion | $(\omega/H)_0<5\times10^{-11}$ | **Assumed from constraint + derived bound** | Eq. (15) text; Appendix F | Don't oversell rotation for expansion |
| Rotation provides preferred axis | Inherits from parent BH | **Assumed (story-level)** | Sec. II.B; Sec. II.C.1 | Separate axis assumption vs measurable prediction |
| Correlated axes between probes | Birefringence axis aligns with spin dipole axis | **Assumed / forecasted** | Abstract; Sec. III.A | Anisotropic spectrum "TBD"; axis-correlation unfinished |

---

## D) CMB Birefringence

| Item | Current Claim | Status | Where | Editor Target |
|------|---------------|--------|-------|---------------|
| Standard rotation formula $C_\ell^{EB}\approx 2\beta(C_\ell^{EE}-C_\ell^{BB})$ | Uses standard formula | **Derived/standard (citation-level)** | Eq. (22) | Fine |
| $\beta = (\alpha/M)D_{\rm inf} f(\tau_{\rm rec})\approx0.30°$ | Claims magnitude tied to parameters | **Fit/Inferred + undefined mapping** | Sec. III.A | From MCMC fits; $f$ undefined; not a derivation |
| "Anisotropic low-$\ell$" component from rotation axis | Claims existence; amplitude "TBD" | **Assumed / not derived** | Sec. III.A | Reframe as speculative |
| Evidence: Planck birefringence 2.4-2.7sigma | Cites Minami & Komatsu + Eskilt | **Fit/Inferred (external)** | Sec. III.A | Fine as observational background |

---

## E) Galaxy Spin Asymmetry

| Item | Current Claim | Status | Where | Editor Target |
|------|---------------|--------|-------|---------------|
| Functional form $A(z)=A_0(1+z)^{-p}e^{-qz}$ | Defines evolution model | **Assumed (phenomenological form)** | Eq. (20) | Not derived from torsion; label as fit ansatz |
| $A_0\propto (\alpha/M)\langle\delta_{\rm rms}\rangle f(z_{\rm form})$ | Claims scaling | **Assumed / heuristic** | Eq. (21) | Needs derivation or label as qualitative |
| $A_0\sim0.003$ | From hierarchical Bayesian fits | **Fit/Inferred** | Sec. II.C.3; Table XI | Correctly admits first-principles pending |
| Dipole axis $(l\sim52°,b\sim68°)$ | Axis claim | **Fit/Inferred (from pipeline)** | Sec. III.B | Needs reproducible catalog + code |
| JWST JADES "15% raw excess" | Included as point; footnoted | **Fit/Inferred (external) + presentation risk** | Fig. 2; Table II | Caveated but plotting invites misuse |

---

## F) Cosmological Parameters, Tensions, Inference

| Item | Current Claim | Status | Where | Editor Target |
|------|---------------|--------|-------|---------------|
| $H_0 = 69.2\pm0.8$, $\sigma_8=0.785\pm0.016$ | Headline numbers | **Fit/Inferred (MCMC)** | Eq. (23)-(24); Table XI | Admit they are fit, not derived |
| "Reduces H0 tension to 1.4sigma" | Claims sigma reduction | **Incorrect / inconsistent** | Table I; Conclusions | Recompute consistently |
| Mechanisms: $\Delta N_{\rm eff}\sim0.2-0.5$, $\Omega_k\sim+0.001$ | Causal story | **Assumed origin + Fit values** | Sec. III.C; Table XI | Inflation-washout contradiction |
| "Not phenomenological degrees of freedom" | Claims bounce microphysics origin | **Overclaim (unsupported)** | Sec. VII.D | Derive or re-label as phenomenological |
| Bayesian evidence $\ln B=+4.8$ | Claims strong evidence | **Fit/Inferred but mislabeled** | Table V; Eq. (38) | Fix dataset labeling inconsistency |
| CAMB modified with $\Lambda_{\rm eff}(z)$ + "bounce ICs" | Claims implementation | **Assumed / under-specified** | Sec. VII.B | Needs equations + code release |
| Reproducibility "bundle in preparation" | Says will release | **Not reproducible yet** | Sec. VII.B | Must exist at posting time |

---

## G) Forecasts / Timeline / Combined Significance

| Item | Current Claim | Status | Where | Editor Target |
|------|---------------|--------|-------|---------------|
| $Z_{\rm comb}$ combination formula | Combines probes with correlation $\rho$ | **Assumed method + bad citation** | Eq. (39); ref [37] | Replace with standard stats reference |
| "5.9sigma by 2034" detection timeline | Forecasted milestones | **Assumed / speculative** | Sec. IX; Table X; Figs 6-7 | Remove or heavily downgrade |

---

## Summary: What the Revised Paper Should Say

* **Derived:** Only what is truly derived (standard results cited, dilution scaling from assumed formula)
* **Assumed:** Model choices (ECH action, parity-odd EFT term, phenomenological $A(z)$, inflationary history)
* **Fit/Inferred:** All numerical cosmology outputs and pipeline outputs unless derived from microphysics
