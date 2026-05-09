# Publication Readiness Master Checklist — All 5 Papers

**Created:** 2026-05-08, ~18:50 PT
**Standing directive:** No shortcuts. No mistakes. Houston Method "full hard fix" for every item below. Nothing in this list is "future work" — every item is in-scope for the loop until shipped.
**Exit definition:** All 5 papers (P1A, P1B, P2, P3, P4) have:
- Zero R-round BLOCKERs in two consecutive review rounds (Claude self-review CCAI + cross-vendor non-Anthropic)
- Zero internal arithmetic / propagation errors
- All forward-cited bibitems defined
- All deferred items either executed or properly scoped
- Houston sign-off

This file is the living source of truth for the publication-readiness work queue. Update it after every commit (mark items DONE / IN PROGRESS) — do not let it drift.

---

## P1A — ECH Structural Closure (no-go theorem) — target PRD

**Current version:** v1A.0.4 (Wave 14-EEEE shipped)
**Honest readiness:** ~70% — strong concept, weak technical core

### MUST-DO before PRD submission

- [ ] **R44-M3 (BIGGEST GAP — gating PRD acceptance):** Four-route no-go currently asserted in one paragraph (§12.2) with sole citation to non-public `Golden2026supplement`. PRD referees will not accept this as a no-go theorem. **Write 3-4 page Appendix C** with one paragraph per route giving derivations + standard citations:
  - **Route (i) NJL condensate**: cite Hehl-Datta 1976 / Hehl-McCrea-Mielke-Ne'eman 1995 review for the contorsion-fermion four-fermion vertex. Repulsivity at γ=0.274 follows from sign of the scalar/pseudoscalar projector. Subcritical for matter densities ≪ Planck; explicit calculation at one density benchmark.
  - **Route (ii) One-loop fermion EA**: cite Mercuri 2008 / Mercuri-Taveras 2009 / Capozziello 2007 for the Barbero-Immirzi parameter renormalization. All γ-dependence in the four-fermion vertex; vanishes at one-loop because Holst term is topological.
  - **Route (iii) Dynamical Immirzi field**: cite Date-Kaul-Sengupta 2009 / Mercuri 2009 / Calcagni-Mercuri 2009. Promotes γ to a scalar; equation of motion gives axion-like dynamics. w analysis: kinetic-dominated regime gives w=+1, V≠0 oscillation gives ⟨w⟩=0 (matter-like), pure slow-roll w=-1. Paper currently says "w=+1 (stiff matter)" which is regime-specific — fix in body too.
  - **Route (iv) Parity-CMB phenomenology**: cite Lue-Wang-Kamionkowski 1999 / Saito et al 2007 for the photon-Holst coupling. Coefficient α/M is what would generate β; explicit absence of this coupling in minimal ECH established by Holst-sector decoupling theorem of §3.
  - Add §10.4 stub-section labels (`sec:oneloopfull`, `sec:condensate`, `sec:cosmo_derivation` at line 443) into proper subsections of this appendix.
- [ ] **R44-M4:** Justify the (T_reh/M_GUT)^{3/2} prefactor in D_inf (§2.3.3 line 367). Either derive (instantaneous reheating + entropy-conserving redshift) or move the prefactor into the marginalized 10^5 fine-tuning bookkeeping with caveat.
- [ ] **R44-M5:** Either populate the orphan `\label{sec:oneloopfull}\label{sec:condensate}\label{sec:cosmo_derivation}` (line 443) with content from the new appendix, or delete the labels + any \ref to them.
- [ ] **R44 minors m1-m4:** c_ω ω² boxed-then-dropped (m1); ~50 vs 92 e-folds bookkeeping (m2); NANOGrav γ canonical citation order (m3); 20% GR-projection citation (m4).

### Cross-paper bibitem cleanup
- [ ] Verify `Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4` are defined in P1A's bibliography with author + year + arXiv placeholder.

---

## P1B — ΛCDM+ΔNeff MCMC + NaMaster + ALP companion — target PRD

**Current version:** v1B.0.1
**Status:** **BLOCKED on cobaya R̂−1 < 0.01** (currently 0.082 at 17:38 PT, ~1-3 days more)
**Honest readiness:** ~85% post-convergence

### MUST-DO

- [ ] **Cobaya DESI DR2 chain → R̂−1 < 0.01** (compute-gated, no acceleration possible)
- [ ] **scp chains to local** `reproducibility/cosmology/chains/w0wa_quintom_desi_dr2/` from pod ijzftpy3klystt
- [ ] **Run `analyze_w0wa_quintom.py`** — extracts w0, wa, p_quintom_B with proper covariance
- [ ] **Update §Structural Tension** in `arxiv/paper1b_mcmc_companion.tex` with the empirical numbers (currently uses April-6 SDSS-DR16 placeholder)
- [ ] **Recompile P1B PDF** (pdflatex × 2 + bibtex + pdflatex)
- [ ] **Mirror to public/papers/ + site/public/papers/**
- [ ] **Bump papers.ts P1B version + pdfMeta**
- [ ] **Bump SSOT/index.md + paper-1/status.md**
- [ ] **Commit Wave 14-XXXX** via plumbing
- [ ] **Run R44-style review on P1B** (it was excluded from R43+R44 because chain in flight)
- [ ] **Apply P1B R44 findings** as Wave 14-YYYY+

---

## P2 — f_NL = -35/8 SPHEREx forecast — target JCAP/PRD

**Current version:** v1.7.12
**Honest readiness:** ~70% — solid groundwork, arithmetic harmonization needed

### MUST-DO before JCAP/PRD submission

- [ ] **R44-B1:** §10.4 "Joint (f_NL, n_fNL) Forecast" reports σ(f_NL) = 0.44 → 9.9σ for marginalized SDB channel — contradicts 3-5σ headline. Either drop the 9.9σ and replace with template+systematic-corrected number, OR explicitly disclose 9.9σ is uncorrected SDB Fisher and reconcile with headline.
- [ ] **R44-B2:** Conclusion §11 "1.5-2.5σ" vs abstract "2.6σ" for convention-flip case. Replace conclusion with "halves from headline 5.2σ to ~2.6σ (template-corrected) or 1.5-2.5σ once GR-marg + b_φ-widening are layered on" and align abstract.
- [ ] **R44-M1:** Bayes factor table tab:bayes — bullet "~17", table "8-11", narrative "17". Add column with multifield prior width per row, reconcile.
- [ ] **R44-M2:** Curvaton competitor prior. Lead with [-5,+5]/σ_theory=1.0 BF (~3-4), demote [-15,+15]/delta to theoretical-maximum upper bound. The current "8-17" abstract is reviewer bait — refuses publication-readiness as written.
- [ ] **R44-M3:** Heinrich convention paragraph (§4) — add explicit normalization equation citation: "Heinrich et al. adopt ζ = ζ_g + (3/5) f_NL ζ_g² (their Eq. X), matching the c=2 convention of Appendix A." Pre-empts the obvious referee question.
- [ ] **R44-M4:** τ_NL = 27.56 saturating Suyama-Yamaguchi: soften to "consistent with single-source non-Gaussianity but does not discriminate bounce from saturated single-source inflationary models." Currently presented as a falsifiable bounce signature, which is a category error.
- [ ] **R44-M5:** DBI as local-shape n_fNL competitor (§10.4 line 356): DBI is equilateral-shape, not local. Replace with axion-curvaton with non-trivial spectral running (Byrnes/Choi/Hall 2010 arXiv:1007.4277) or quasi-single-field inflation (Chen-Wang 2010).
- [ ] **R44 minors m1-m3 + nit1:** Decompose "3-5σ realistic" into one row table (m1); reconcile +10-20% improvement vs −15-30% degradation for anomaly tracers (m2); Jung+2025 PR4 "tightens by ~2%" cross-check (m3); release tag `v1.7.10-paper2` → `v1.7.13-paper2` at /ship time (nit1).
- [ ] **Pre-existing Maldacena:2003 undef cite** — fix bibitem (residual from R43).

### Cross-paper bibitem cleanup
- [ ] Verify `Golden2026P1a`, `Golden2026P3`, `Golden2026P4` defined in P2's bib.

---

## P3 — 378K-anomaly multi-survey catalog — target ApJS

**Current version:** v3.1.23
**Honest readiness:** Catalog 90% / f_NL section 50% — mixed

### MUST-DO before ApJS submission

- [ ] **R44-M1:** Conclusions §6.5 still says "improve σ(f_NL) by ~6-20%" — pre-VVV claim contradicts demoted abstract. Replace with central-value-forecast language.
- [ ] **R44-M2:** §VII has both demoted 8.27 AND legacy 6.1%/16.4% positive claims side-by-side. Subordinate the legacy 6.1% to "for reference only" or delete.
- [ ] **R44-M3 (BIGGEST P3 ISSUE):** Three different σ(f_NL) normalizations live in the paper, differing by a factor of ~250×:
  - (a) §VII headline: σ(f_NL) = 8.27 ± 2.37
  - (b) §VII Wave 14-II marginalized: σ(f_NL) = 0.067-0.116
  - (c) Appendix B.1 shot-noise: σ(f_NL) = 11.71 / 12.72 / 16.85
  - The 11.71-16.85 family is **confabulated** per CLAUDE.md fire #25 (acknowledged correction never propagated). **Fix:** delete App. B.1 / Fig. B11 entirely, OR rewrite using Heinrich+2023 σ(f_NL)=0.7 anchor and explain the ratio between (a), (b), (c) explicitly.
- [ ] **R44-M4:** "Primary tier" defined two ways. Adopt:
  - "point-source tier" = 378,080
  - "catalog-grade tier" = 264,938 (excludes LAMOST exploratory)
  - "exploratory tier" = LAMOST 113,342
  - Audit every "primary" mention against this taxonomy.
- [ ] **R44-M5 (load-bearing):** Wave 14-VVV α_jk = 0.19 ± 0.65 measured at low ⟨z⟩ (only 12 of 5,384 candidates spec-confirmed at z≈6); inserted into z>0.8 SPHEREx Fisher pipeline. The σ(f_NL) = 8.27 figure is "a number without meaning" at the SPHEREx multi-tracer regime. **Two paths**:
  - **Path A (cheap):** Demote to "illustrative central-value insertion only; not a forecast at the redshift relevant to SPHEREx multi-tracer f_NL" — explicit caveat in abstract + §VII.
  - **Path B (thorough — preferred per "no shortcuts"):** Run high-z restricted re-analysis on the spec-confirmed 12-object subset + photometric-z proxy on the rest. Ship empirical α at proper redshift. Local CPU runs in 1-2 hours.
- [ ] **R43-M5 (carried forward):** Anomaly-window-randoms methodology paragraph not in paper. Add half-page methodology paragraph in §VII or new Appendix C documenting:
  - Random catalog construction (anomaly footprint mask, no z-weighting since we project)
  - 30 jackknife regions definition (sphere-tessellation from anomaly RA/Dec via cKDTree, equal-N partition)
  - Per-bin Δw(θ) and how the geomean over 3 bins is computed
- [ ] **R44 minors m1-m5 + nits:** α_geo vs α_jk difference explained with finite-N JK bias note (m1); "consistent with α=0.15 within 1σ" rephrased to "within 0.06σ" with honest CI [-1.08, +1.46] note (m2); SDSS 77,905 in dedup arithmetic — defend or recompute (m3); CMB val_loss 0.4437 fails criterion (a) disclosed (m4); NANOGrav γ project SSOT alignment (m5); "Munchmüller" → "Münchmeyer" spelling (nit1); 637 multi-survey clusters dominated by LAMOST FAIL caveat (nit2).

### Cross-paper bibitem cleanup
- [ ] Verify `Golden2026P1a`, `Golden2026P1b`, `Golden2026P2`, `Golden2026P4` defined in P3's bib.

---

## P4 — 8.47M galaxy chirality at scale — target MNRAS

**Current version:** v1.0.32
**Honest readiness:** ~85% — closest to publishable

### MUST-DO before MNRAS submission

- [ ] **R44-M1:** p_LEE harmonization. Three sites currently inconsistent:
  - Abstract: "p_LEE < 10^-4 at MC resolution floor"
  - §V.A line 1987: "p_LEE = 9.999×10^-5"
  - Footnote 12: "p_LEE = 1/(N_MC+1) = 9.999×10^-5"
  - **Fix:** All three → "p_LEE ≤ 1/(N_MC+1) ≈ 1×10^-4 (one-sided 95% upper bound ≈ 3×10^-4 by Clopper-Pearson, given 0/10,000 exceedances)."
- [ ] **R44-M2:** GZ1 Platt "identical to 4 sig figs" claim is suspicious — A=1/4.65=0.2151 typed twice. Two independent L-BFGS fits on different label sets essentially never converge to identical parameters. Either (a) actually rerun the GZ1-only fit with proper random init and report 6 sig figs of difference, or (b) drop the identity claim and rely on the binomial-difference test alone.
- [ ] **R44-M3:** GZ1 binomial uses wrong unpaired SE √(2 p(1-p)/N). Both samples are PAIRED on 46,017 matched galaxies. Replace with McNemar's paired test:
  - Compute b = #(GZ1 says CW, Catalog C says CCW), c = #(GZ1 says CCW, Catalog C says CW)
  - McNemar χ² = (b-c)²/(b+c)
  - Recompute Z; expect ~7-8σ for the same gap (paired SE is smaller than unpaired)
  - Update the monopole-floor framing accordingly (the gap is real, just understated as 5.5σ)
- [ ] **R44-M4:** Recall asymmetry (CW 93.8% vs CCW 92.6%) and GZ1 1% bias double-counted. Decompose: (93.8-92.6)/(93.8+92.6) ≈ 0.64% predicted from recall asymmetry alone, vs 0.79% observed — leaves only 0.15% for GZ1-prior contribution. Make §IV.A "three candidate mechanisms" mutually exclusive.
- [ ] **R44-M5 (1-pod-hour, NOT future work):** Deep-MLP RA/Dec ablation. Retrain deep MLP on the same morphology features but **without** RA/Dec inputs, report AUC drop. If still > 0.55: coupling is morphology-real. If drops to ≈ 0.50: RA/Dec was doing the work and per-pixel projection is mandatory. Ship to pod when cobaya finishes (or run on local Mac in parallel).
- [ ] **R44-M6:** §IV.B MDD = 0.2% assumes independent pixels. §IV.A warns N_eff < N_spiral due to spatial correlations in seeing/PSF/depth. State MDD as "0.2% assuming independent classifications; N_eff corrections may inflate to 0.3-0.4%." Update abstract too.
- [ ] **R44-M7:** 3-of-4 morphology axes FAIL 0.1% CW-flatness target at 10-bin granularity (size 0.32%, fracdev 1.41%, b/a 0.23%). Add to abstract: "morphology bin flatness fails at 0.3-1.4% at 10-bin granularity (size, fracdev, b/a); these spreads are spatially uniform but ceiling per-morphology-bin dipole sensitivity, not global dipole sensitivity." Or: do dipole analysis split by morphology bin, report worst-case bin's MDD.
- [ ] **R44 minors m1-m5 + nits:** "−0.12σ" signed-significance meaningless (m1); N_MC=1,000 dipole vs 10,000 hemisphere inconsistent (m2); 69.91% spiral accuracy → CW-bias propagation (m3); GZ1 ACW=CCW orientation convention post-Iye+2020 (m4); Platt is target-shift not bias-reduction (m5); abstract paren-mismatch typo (nit1); stray "PUSHBACK" prose token in §III.F (nit2).

### Cross-paper bibitem cleanup
- [ ] Verify `Golden2026P1a`, `Golden2026P1b`, `Golden2026P2`, `Golden2026P3` defined in P4's bib.

---

## Cross-paper bookkeeping

- [ ] **Bibliography keys for cross-references:** Each paper cites the others as `Golden2026P{1a,1b,2,3,4}`. Audit each paper's bibliography for the four other-paper bibitems. Add author + year + arXiv-placeholder + "(in preparation)" or "(submitted)" once submission targets known.
- [ ] **Houston-only items (NOT autonomous loop scope; tracked but Houston-owned):**
  - P1-RHAT-NUMBER-RECONCILE — scientific-judgment call on R̂ reporting convention
  - P1-BETA-EQ38-CHECK — manual β prediction check at Eq. 38
  - P3-PATHC-LAMOST-98PCT-CORRECTION — LAMOST 98% blue-excess correction
  - arXiv submissions (5 papers, you have the login)
  - HuggingFace dataset visibility flip for P3 (you have dashboard access)
- [ ] **Cross-vendor adversarial review (per memory `feedback_cross_model_peer_review.md`):** Mandatory non-Anthropic peer review before submission. The R44 prompt is in chat history. Paste into fresh sessions of:
  - ChatGPT-5 (one session per paper)
  - Gemini 3.1 Pro (one session per paper)
  - Grok-4 (one session per paper)
  - Perplexity (cross-check on bibliography + recent literature)
  - Save findings to `project-context/peer-reviews/<date>_R44+_crossvendor_*.md`
  - Apply cross-vendor findings using same Wave 14-AAA workflow.
  - **No paper ships to arXiv until cross-vendor R-round returns < 3 BLOCKER + < 5 MAJOR total.**

---

## Loop discipline

- Every iteration: kill git zombies, check cobaya chain, apply next batch.
- Per-paper recompile + mirror + bump version + commit per Wave letter.
- Use Write tool for commit messages (NOT heredoc — nested LaTeX braces break zsh parser).
- Use `/opt/homebrew/bin/timeout` (NOT `/usr/bin/timeout`).
- Mark items DONE in this file as they ship; **do not let this list drift.**

---

## Wave letter assignments (planned)

- ✅ Wave 14-WWW: P3 v3.1.22 R43 BLOCKERs B1+B2+B3 + M3 + m1
- ✅ Wave 14-XXX: P4 v1.0.31 R43 BLOCKERs B1+B2 + M4
- ✅ Wave 14-YYY: P2 v1.7.11 R43 BLOCKER B2
- ✅ Wave 14-ZZZ: P1A v1A.0.2 R43 BLOCKERs B1+B2+B3
- ✅ Wave 14-AAAA: P1A v1A.0.3 R43 MAJORs M2+M4+M5/M6
- ✅ Wave 14-BBBB: P4 v1.0.32 R43 MAJOR M3
- ✅ Wave 14-CCCC: P3 v3.1.23 R43 MAJOR M4 + m1
- ✅ Wave 14-DDDD: P2 v1.7.12 R43 MAJORs M1+M2 + bib entries
- ✅ Wave 14-EEEE: P1A v1A.0.4 R44 BLOCKERs B1+B2+B3 + M1+M2 + R44 review file saved
- 🔜 Wave 14-FFFF: P3 R44 M1+M2+M4 + nit1 + P3 minors
- 🔜 Wave 14-GGGG: P4 R44 M1+M2+M3 + nits + P4 minors (and the RA/Dec ablation if compute available)
- 🔜 Wave 14-HHHH: P2 R44 B1+B2+M1+M2+M3+M5 + minors
- 🔜 Wave 14-IIII: P1A R44 M3 four-route appendix + M4+M5+m1-m4
- 🔜 Wave 14-JJJJ: Cross-paper bibitem cleanup pass (Golden2026P{1a,1b,2,3,4} in each)
- 🔜 Wave 14-KKKK: P3 high-z restricted α re-measurement (R44-M5 Path B)
- 🔜 Wave 14-LLLL: P4 deep-MLP RA/Dec ablation (R44-M5)
- 🔜 Wave 14-MMMM: R45 Claude self-review on post-Wave-LLLL versions
- 🔜 Wave 14-NNNN+: Cross-vendor (GPT-5 / Gemini / Grok / Perplexity) findings application
- 🔜 Wave 14-XXXX: P1B post-cobaya §Structural Tension update (compute-gated)
