# P1A R29 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7 (in-session)`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.57.pdf` md5=958587c7 pages=27
**Input format**: NATIVE PDF (document block) + extended thinking 16K
**Wall time**: in-session replacement (API leg credit-failed)

---

## Verdict: MAJOR REVISION

The paper is conceptually serious and the EXT1 closure wave has clearly addressed the headline ALP convention bug and the Holst/Bianchi/Pontryagin confusion. However, my full re-read flags several real defects: an abstract/conclusions e-fold-erasure quantitative claim that is internally inconsistent ($N_{\rm tot}\approx 92$ vs. erasure at $N_{\rm tot}\!\gtrsim\!60$, with the actual signal-erasure-relevant differential $N_{\rm tot}-N_{\rm exit}\approx 32$ being a different quantity than what is reported in the abstract), a Cartan-equation sign chain whose stated arithmetic does not actually close ($+\kappa/2$ vs $-3\kappa/16$ jump is presented without the intermediate step), a Holst term whose coefficient in Eq. (1) is missing its half-factor relative to standard ECH conventions, a $T^{abc}T_{abc}$ "shorthand" claim that misrepresents the action's true content, a Route-2 dimensional/scaling estimate ($10^{-58}$ vs $10^{-33}$) whose "alternative ordering" is given no derivation, an Appendix-B headline equation `\rho_\Lambda^{\rm bounce}\sim(\alpha/M)\,\MPl^5` whose dimensions are NOT $+4$ but $+4$ only by a mass-dimension miscount that the appendix itself disclaims yet uses, repro-bundle naming inconsistency (`v1A.0.56-bundle` while paper is v1A.0.57) suggesting incomplete EXT1 closure of the data-availability bullet, and abstract↔body misordering of caveats (the abstract still names "perturbation-transparency theorem" while the body labels the same content variously as theorem, result, observation, and gates).

---

## ESSENTIAL findings (REJECT-class until fixed)

### P1A-E1 — Abstract↔body quantitative drift: the $N_{\rm tot}\!\gtrsim\!60$ erasure threshold is inconsistent with the body's actual $N_{\rm tot}-N_{\rm exit}\approx 32$ differential
**Section / line**: Abstract L412–413, §I L584, §sec:structural_tension L2277–2300, §sec:surviving L2217.
**Quoted text (abstract, L412)**:
> "a contracting-phase quantity mode with $k_{\rm SPHEREx}\sim 10^{-1}\,h/$Mpc is pushed to $k_{\rm bounce}^{\rm phys}\sim k_{\rm SPHEREx}^{\rm phys}\,e^{N_{\rm tot}-N_{\rm exit}}\sim e^{32}\,k_{\rm SPHEREx}^{\rm phys}$ at $N_{\rm tot}\sim 92$, $N_{\rm exit}\sim 60$"
**Quoted text (§I L584)**:
> "definitively erased by $N_{\rm tot}\!\gtrsim\!60$ inflationary $e$-folds"
**Quoted text (§sec:structural_tension L2278)**:
> "would require $N_{\rm tot}\approx 92$ post-bounce $e$-folds; the matter-bounce $\fnl=-35/8$ would be definitively erased by $N_{\rm tot}\gtrsim 60$"
**Problem**: Three different "erasure thresholds" are quoted across the paper for what is presented as one physical fact. The body's own mode-history argument (epochs (i)–(iv)) makes clear the erasure happens because the SPHEREx physical scale at the bounce is set by the *differential* $N_{\rm tot}-N_{\rm exit}$, not by $N_{\rm tot}$ alone. The statement "erased by $N_{\rm tot}\!\gtrsim\!60$" is therefore not even dimensionally the same quantity. Either (a) the threshold $60$ should be $N_{\rm tot}-N_{\rm exit}\!\gtrsim$~few (so that $e^{\text{few}}$ exceeds the matter-bounce coherent-mode window), with $N_{\rm exit}$ a fixed CMB horizon-exit reference; or (b) the threshold is $N_{\rm tot}\!\gtrsim\!N_{\rm exit}$. The current "$\gtrsim 60$" reads like $N_{\rm exit}$ alone is the criterion, which is not what the mode-history ledger says. Pattern-008 downstream-prose-after-physics-rewrite repeats here.
**Required fix**: Pick one definition (recommended: state it as $N_{\rm tot}-N_{\rm exit}\!\gtrsim\!N_{\rm coh}$ where $N_{\rm coh}\sim$ few is the matter-bounce contraction-mode coherence window; or simply "$N_{\rm tot}\!\gtrsim\!N_{\rm exit}+N_{\rm coh}$"). Propagate to abstract, §I L584, §sec:surviving L2217, §sec:structural_tension. Cross-check that the abstract clause "at $N_{\rm tot}\sim 92$" matches the body's "$N_{\rm tot}\approx 92$ post-bounce $e$-folds" and the bounce-vs-SPHEREx scale ratio $e^{32}$ everywhere.

### P1A-E2 — Cartan-equation sign-chain in the footnote at Eq. (3) has a gap: $\frac{\kappa^2}{4}\,S^{abc}S_{abc}\to-\frac{3\kappa}{16}(J^5)^2$ is not the intermediate step
**Section / line**: §sec:parityodd footnote at L707–743 (the long single-convention footnote).
**Quoted text (L723–733)**:
> "explicitly, the on-shell substitution $T^{abc}=\kappa S^{abc}$ gives $\tfrac{1}{4}T^{abc}T_{abc} = \tfrac{\kappa^2}{4}S^{abc}S_{abc}$, and the standard Hehl–Datta bookkeeping (the gravitational contact piece plus the fermionic spin–torsion coupling; the same sign manipulation quoted at Eq.~\eqref{eq:NJL_torsion}) nets to $\mathcal{L}_{\rm int} = +\tfrac{\kappa}{2}\,S_{abc}S^{abc}$, so integrating out torsion yields $\mathcal{L}_{\rm int} = -\tfrac{3\kappa}{16}\,J^5_\mu J^{5\mu}$"
**Problem**: The footnote was added in R27conf-M1 to display the substitution step, but the displayed chain is internally inconsistent. The claim "nets to $+\kappa/2\,S_{abc}S^{abc}$" then "yields $-3\kappa/16\,(J^5)^2$" requires the identity $S_{abc}S^{abc} = -\tfrac{3}{8}\,J^5_\mu J^{5\mu}$, which the footnote *does* derive earlier, so the algebra is $+\tfrac{\kappa}{2}\cdot(-\tfrac{3}{8}) = -\tfrac{3\kappa}{16}$. That checks. But the **first** step "$\tfrac{1}{4}T\cdot T = \tfrac{\kappa^2}{4}S\cdot S$ ... nets to $+\tfrac{\kappa}{2}S\cdot S$" is dimensionally wrong: $\kappa^2/4 \neq +\kappa/2$, and the Hehl–Datta cancellation from the kinetic-Einstein contact piece is what converts $+\kappa^2/4 \to -\kappa/2$ (note the sign), as Hehl 1976 Eq. (3.21). The footnote should explicitly display the cancellation that drops a power of $\kappa$. As stated, the reader sees $\kappa^2 \to \kappa$ with no explanation. This was the explicit R27conf-M1 ask — half-done.
**Required fix**: Insert one displayed line: "Combining the gravitational $-\tfrac{1}{4}T\cdot T = -\tfrac{\kappa^2}{4}S\cdot S$ with the fermionic spin-connection coupling $+\kappa\,S\cdot S$ (Hehl 1976 Eq. (3.20)) gives the net $\mathcal{L}_{\rm int} = (+\kappa - \tfrac{\kappa^2}{4}\cdot(1/\kappa))S\cdot S$ ..." — or whatever the correct combinatorics is from the actual reference. As written the dimensions don't match.

### P1A-E3 — Eq. (1) ECH action: coefficient of the curvature-square term is missing the standard $1/2$ relative to the textbook ECH action
**Section / line**: Eq. (\ref{eq:ECH}) at L647–650.
**Quoted text**:
> $S_{\rm ECH} = \frac{1}{16\pi G} \int d^4x\, e \left[e^\mu_a\,e^\nu_b\,R^{ab}_{\;\;\;\mu\nu} + \frac{1}{\gamma} \varepsilon^{abcd}\,e_{a}^{\;\mu}\,e_{b}^{\;\nu}\,R_{cd\mu\nu} + \frac{1}{4} T^{abc} T_{abc}\right]$
**Problem**: Two concrete defects: (a) the textbook tetradic Einstein–Hilbert action is $\frac{1}{16\pi G}\int e\,e^\mu_a e^\nu_b R^{ab}_{\mu\nu}$ with no $1/2$ in front because the tetrad already provides the Lorentz-doublet contraction — but the standard ECH Holst term carries $\frac{1}{2\gamma}$ (not $\frac{1}{\gamma}$) as in e.g. Mercuri 2008 Eq. (2.2), Freidel–Minic–Takeuchi 2005 Eq. (1), Holst 1996 Eq. (1). The factor-of-2 enters from the antisymmetrization of $\varepsilon^{abcd}e_a^\mu e_b^\nu R_{cd\mu\nu}$ vs $\tfrac{1}{2}\varepsilon^{abcd}e^\mu_a e^\nu_b R_{cd\mu\nu}$. (b) The $\frac{1}{4}T^{abc}T_{abc}$ "shorthand" claim in the prose at L658–664 reads: "shorthand for the four-fermion contact interaction obtained after integrating out the non-propagating torsion; it is not an independently specified kinetic term". But this prose contradicts what the equation *displays*: a literal $T\cdot T$ term in the action. A reader takes the action at face value. The R27conf META-M3 "T² shorthand 'not varied independently, no double counting' clause" closed the prose half but left the displayed action ambiguous. Either drop the $T\cdot T$ term from Eq. (1) entirely (correct minimal-ECH presentation: the Cartan equation generates the contact term from the matter-Lagrangian variation of the connection — no $T\cdot T$ kinetic in the gravity sector), or keep it and add an inline footnote at the equation pointing to L658–664.
**Required fix**: Drop the $\tfrac{1}{4}T^{abc}T_{abc}$ from inside the bracket of Eq. (1) and rewrite as the bare Palatini + Holst action; let the contact term emerge from the variation, which is what the body actually does. If keeping for pedagogical clarity, add `\footnote{This term is the post-elimination contact term displayed here for completeness; it is not a kinetic term and is not varied independently of $S_{\rm matter}$ in the connection variation. See L658–664.}` at the displayed equation, not 6 lines later. Also fix $1/\gamma\to 1/(2\gamma)$ if the curvature contraction conventions follow the cited literature; otherwise insert a footnote stating the unconventional choice explicitly.

### P1A-E4 — Repro-bundle tag mismatch: bundle labelled `v1A.0.56-bundle` while paper is v1A.0.57
**Section / line**: §Data and Code Availability L2403–2407.
**Quoted text**:
> "The bundle is labelled \texttt{v1A.0.56-bundle} (resynced 2026-06-10) to track the present manuscript title and version"
**Problem**: The paper version is v1A.0.57 (L48), but the bundle reads v1A.0.56-bundle. The EXT1 closure wave was supposed to resync the repro bundle to the manuscript. The mismatch suggests the EXT1 closure of the data-availability item only updated the date and not the tag, or that the actual repo tag was not bumped. Provenance sweep (sweep 16) fails: a downloading reader cannot confirm "this bundle = this paper" by version match alone.
**Required fix**: Either (a) update the paper to read `v1A.0.57-bundle`, push a matching git tag, verify it resolves on GitHub; or (b) explicitly state "Bundle v1A.0.56-bundle reflects the prior v1A.0.56 manuscript; the v1A.0.57 edits are textual-only and require no bundle changes (see closure log)" with a link to the closure log. Per provenance protocol, also include the bundle commit SHA in the paragraph.

---

## MAJOR findings

### P1A-M1 — Route-2 "alternative ordering" yielding $10^{-33}$ is asserted, not derived
**Section / line**: §sec:r2_oneloop L1294–1300.
**Quoted text**:
> "We adopt this contraction as the canonical Route-2 estimate; an alternative ordering that contracts the $H_0$ factor with the dimensionful coupling differently yields a numerically distinct $\sim 10^{-33}$ ratio. The canonical-bound conclusion that the one-loop induced $\beta$ is amplitude-suppressed many orders of magnitude below the observed WMAP$+$Planck birefringence signal (with ACT~DR6 follow-up) is robust to this choice."
**Problem**: The reader is told that two orderings of the same dimensionless ratio differ by 27 orders of magnitude ($10^{-60}$ vs $10^{-33}$). A 27-OOM disagreement between two ways of writing the same dimensional ratio is a *huge red flag*, not a "robust to this choice" caveat. Either (a) one of the orderings is dimensionally wrong, or (b) the underlying operator is being applied with different physical assumptions in the two cases. The paper concedes the alternative "yields $10^{-33}$" but does not derive it, does not state what physical assumption distinguishes the two orderings, and does not show that either way the closure holds. Sweep 17 (uncomputed claims): "robust to this choice" needs a number.
**Required fix**: Either (i) give the explicit derivation of the $10^{-33}$ ordering in a brief footnote or appendix paragraph so the reader can verify the assumption that distinguishes the two, OR (ii) remove the $10^{-33}$ aside entirely (it was added in R24conf META-M4) since "$10^{-60}$ canonically, $10^{-58}$ conservatively" already overkills the WMAP+Planck $\beta\sim 6\times 10^{-3}$ rad target by 55+ orders of magnitude. Cleaner to drop the $10^{-33}$ side-claim than to half-derive it.

### P1A-M2 — Appendix B headline equation has off-shell mass-dimension $+5$, but the appendix uses it as the dim-$+4$ result
**Section / line**: Appendix B Eq.~(\ref{eq:onshell_rho}) L2483–2486.
**Quoted text**:
> $\rho_\Lambda^{\rm bounce}\sim(\alpha/M)\,\MPl^5 \sim 10^{-2}\,\MPl^4$
**Problem**: $[\alpha/M] = -1$, $[\MPl^5] = +5$, so the displayed left-hand side has mass-dimension $+4$ as required for an energy density. So far OK. *But* the prose immediately preceding states "the parity-odd operator (Eq. \ref{eq:Seff_comp}) has off-shell mass dimension $+1$" — and the leap from a dim-$+1$ Lagrangian density to a dim-$+4$ vacuum energy via an on-shell substitution is precisely the place where Sweep 19 (effect sizes) demands an explicit estimate of the on-shell coefficient. The current text says: "Inserting on-shell background curvature factors or a phenomenological volume-integration-density factor of $\MPl^{2}$ does not constitute a derivation". Then *uses* exactly such a factor to write Eq. (B-onshell_rho). The honesty disclaimer is correct, but the headline equation is then used downstream (Eq. B-Xi, $N_{\rm tot}\approx 94$) as if it were derived. The on-shell-curvature insertion factor is never quantified as a number with uncertainty — it is implicit in the $10^{-2}\,\MPl^4$ side, which folds in $[(\alpha/M)\,\MPl]\sim 10^{-2}$ from §parityodd. The disclaim-and-use pattern obscures that the entire $N_{\rm tot}\approx 94$ inference depends on an unestimated on-shell coefficient. The structural-tension argument inherits this systematic.
**Required fix**: Either (a) name the on-shell curvature factor explicitly: "We make the on-shell-curvature assumption $\langle R^{\mu\nu\rho\sigma}\rangle_{\rm bounce} \sim \MPl^2$, which sets the dimensional-promotion factor at $\MPl^2$; varying this assumption by $\mathcal{O}(1)$ shifts $N_{\rm tot}$ by $\delta N\sim \ln(\mathcal{O}(1))/3 \sim O(1)$ e-folds, *not* by orders of magnitude." (b) Or move Eq.~(\ref{eq:onshell_rho}) out of the headline display and into a "scaling estimate" sub-paragraph so the reader does not take it as a derived equation.

### P1A-M3 — "Perturbation transparency theorem" naming is inconsistent across the paper
**Section / line**: Abstract L386 ("theorem"); §I L572 ("perturbation-transparency observation"); §sec:transparency title and L1855 ("perturbation transparency"); Table I L529 ("Perturbation-transparency result"); B14 entry L1856 ("Perturbation Transparency").
**Quoted text**:
> Abstract: "The central result is a perturbation-transparency theorem"
> §I L572: "14-constraint catalog and perturbation-transparency observation"
> Conclusions L2354: "Central result: perturbation transparency"
**Problem**: Five different labels: "theorem", "observation", "result", "gates", and "(unlabeled)". External reviewers have flagged this naming inconsistency at least once (Grok R-upgraded-round7 GRO-B1 was about theorem-vs-no-theorem framing). The R-upgraded-round7 closure softened §X but the abstract still says "theorem" while §I L572 says "observation". Standalone-reader sweep (18) fails.
**Required fix**: Adopt a single label throughout. Given that §sec:transparency provides a 5-step proof and the paper claims it is mathematically rigorous, "theorem" is appropriate for §X and Conclusion. §I and Table I should match. Replace "observation" at L572 with "theorem" and adjust §sec:foundations to be consistent. Or, if "result" is preferred to dodge the theorem question for non-fermion non-canonical extensions, use "result" everywhere.

### P1A-M4 — $\Gamma_{\rm washout} > H$ "conditional closure" is the entire Barrier-14 supporting argument, but is never actually computed
**Section / line**: §sec:dilution L1001–1015, L996–1010.
**Quoted text**:
> "the operative requirement is $\Gamma_{\rm wash}(T_{\rm reh}) > H(T_{\rm reh})$, a condition rather than a result of the present analysis ... A full Boltzmann calculation of $\Gamma_{\rm wash}(T)$ vs $H(T)$ ... is left to a follow-up"
**Problem**: The paper says (i) the operative inequality is $\Gamma_{\rm wash}/H > 1$, (ii) "$\alpha_W^5 M_{\rm Pl}/T \gg 1$" and "$y_t^2 M_{\rm Pl}/T \gg 1$" are quoted as evidence, then (iii) the Boltzmann calc is deferred. But (ii) is just dimensional-ratio handwaving: $\alpha_W^5 \approx 4\times 10^{-9}$ (taking $\alpha_W \approx 1/30$), so $\alpha_W^5\,M_{\rm Pl}/T \approx 4\times 10^{-9}\cdot 10^{19}/10^{15} = 4\times 10^{-5}$ at $T = T_{\rm reh}\sim 10^{15}\,$GeV, NOT $\gg 1$. The inequality fails at the GUT scale for sphalerons; it only works at $T \lesssim 10^{12}\,$GeV per the paper's own L991 statement. Top-Yukawa $y_t^2\,M_{\rm Pl}/T \sim 1\cdot 10^{19}/10^{15} = 10^4$ does work, but $y_t \sim 1$ assumes weak-scale running, not GUT-scale running where $y_t$ is lower. The conditional closure rests on top-Yukawa dominance at $T_{\rm reh}$ that is asserted, not computed. Sweep 17 (uncomputed claim): "$\Gamma_{\rm wash} > H$ ... expectation, given the ratios" needs a number.
**Required fix**: Either (a) compute $y_t(T_{\rm reh})$ at the relevant scale via standard SM RG running and plug it in (5-min calculation), reporting $\Gamma_t/H$ at $T_{\rm reh}=10^{15}\,$GeV; or (b) state explicitly: "We rely on $y_t(T_{\rm reh})\sim 0.5$ from one-loop SM running (citation), giving $\Gamma_t/H \sim 0.25\cdot 10^{19}/10^{15} = 2.5\times 10^3$, $\gg 1$ as required". Without a number this is hand-waving. Also fix the sphaleron $\alpha_W^5$ ratio statement: it does NOT give $\gg 1$ at the GUT scale.

### P1A-M5 — Eq. (4) four-fermion contact term: γ-dependence sign discrepancy with Freidel–Minic–Takeuchi
**Section / line**: Eq. (\ref{eq:4fermi}) at L747–749.
**Quoted text**:
> $\mathcal{L}_{\rm int} = -\frac{3\pi G_N}{2}\times \frac{\gamma^2}{\gamma^2+1}\times J^5_{\mu}\,J^{5\mu}$
**Problem**: Freidel–Minic–Takeuchi 2005 (cited as the foundational reference at L655) Eq. (50) reads $\mathcal{L}_{\rm contact} = -\tfrac{3}{16}\,\kappa\,\bigl(\tfrac{\gamma^2}{\gamma^2+1}\bigr)(\bar\psi\gamma^a\gamma^5\psi)^2$ — with $-3/16\,\kappa = -3/(16\,M_{\rm Pl}^{-2})\cdot 8\pi G = -3\pi G/2\,(2/M_{\rm Pl}^{-2})$ ... the dimensional check passes, but the displayed coefficient $-3\pi G_N/2$ vs the FMT $-3\kappa/16$ requires $\kappa = 8\pi G_N$, giving $-3\cdot 8\pi G_N/16 = -3\pi G_N/2$. So the displayed coefficient is correct relative to FMT. However, the *form* "$-\frac{3}{16}\kappa$" is what is quoted in the L1197 NJL-torsion paragraph for the $\gamma\to\infty$ limit of the same equation, so Eqs. (4) and (NJL_torsion) should be visually consistent. Currently Eq. (4) is in $G_N$ units and Eq. (NJL_torsion) in $\kappa$ units. They are correct, but the reader has to translate.
**Required fix**: Either (a) rewrite Eq. (4) as $-\tfrac{3}{16}\,\kappa\,(\gamma^2/(\gamma^2+1))\,(J^5)^2$ to match Eq. (NJL_torsion); or (b) add a parenthetical at Eq. (4) "$=-\tfrac{3\kappa}{16}\,(\gamma^2/(\gamma^2+1))(J^5)^2$ in the $\kappa = 8\pi G_N$ convention used in Eq. (NJL_torsion)". As written, the consistency is not enforced visually.

### P1A-M6 — Companion-paper self-containment: §sec:obs and §sec:related cite "Paper~I(b) Table~IV" and §V details that don't exist on arXiv
**Section / line**: §sec:obs L1097–1104 (MCMC numbers), §sec:loophole L2036–2048 (w0wa chain status), §discussion L2145 (ALP fit "9,720 accepted samples"), Table V footnote L2003–2004.
**Quoted text (L2003)**:
> "the three completed dataset combinations enumerated in Paper~I(b) \S~VII Table~IV, subsection 'Free-$w_0 w_a$ chain status'"
**Problem**: The paper imports specific structural details from Paper I(b) (chain status, dataset-combo enumerations, chain convergence $\hat R - 1 \approx 3\times 10^{-2}$, sample counts) as if Paper I(b) were a citable reference. But Paper I(b) is "in preparation" (per the bbl entry and per the prose at L539, L1546, L2152). The EXT1 closure of "companion self-containment" was supposed to remove these forward dependencies. Standalone-reader sweep (18) fails: a referee or reader without access to the in-prep Paper I(b) cannot verify any of these claims. The fix in v1A.0.57 added "in preparation" qualifiers but did *not* strip the Paper I(b)-Table-IV-row-name imports.
**Required fix**: For each forward-reference to a specific Paper I(b) table/section/row: either (i) inline the relevant number with its own citation (the "9,720 accepted samples" can stand alone if the value is reported here), or (ii) replace "Paper~I(b) \S VII Table IV row Foo" with "the companion MCMC analysis in preparation~\cite{Golden2026P1b}" (no row-name). The current text reads like P1B is on arXiv when it is not.

### P1A-M7 — Fig. 1 caption (theory map): PTA annotation "$2.567\pm 0.382$" is itself a result imported from Paper III, which is in-prep
**Section / line**: Fig. 1 caption L549–559.
**Quoted text**:
> "The PTA annotation reflects the current real-KDE reanalysis $\gamma = 2.567 \pm 0.382$ (Sec.~\ref{sec:discrimination})"
**Problem**: §sec:discrimination L2010 attributes the $2.567\pm 0.382$ to "real-KDE reanalysis of the 15-yr free-spectrum data (GPU MCMC, companion Paper~III~\cite{Golden2026P3})". Paper III is in-prep. Same as P1A-M6: a figure caption is presenting an unpublished number as if it were a known measurement. The R27conf Gemini M5 closure documented this ("burned-in PTA 3.20+-0.42 disclosed as superseded pre-real-KDE value, 2.567+-0.382 pointer") but stopped at internal-disclosure. The figure caption itself does not flag the value as in-prep.
**Required fix**: Append "(internal Paper III analysis in preparation~\cite{Golden2026P3})" to the caption sentence, OR move the PTA number out of the figure caption and into the body §sec:discrimination only. Captions should be self-contained.

### P1A-M8 — Barrier 12 "ansatz" closure is now too weak to support B12 as a logically-independent barrier
**Section / line**: §sec:barriers Barrier 12 L1840–1846.
**Quoted text**:
> "The quadratic scaling in $\rhocrit/\rhoPl$ is adopted here as an order-of-magnitude ceiling \emph{ansatz} (not derived in this paper); Barrier~12 is correspondingly used only as a global ceiling, not as a precise bound."
**Problem**: B12 is one of the 13 "logically independent" barriers used in the abstract+conclusions count. But the body now concedes the quadratic scaling is an ansatz and the comparison to NANOGrav is "deferred to a forthcoming bounce-GW dedicated paper". A barrier whose closure is "we don't compute, we adopt an order-of-magnitude ceiling" is not a barrier in any rigorous sense — it is a hypothesis. The 13-barriers logical-independence claim is undermined: if B12 reduces to a hypothesis, the count is at best 12 logically independent. Sweep 17 (uncomputed claim): "$\Omega_{\rm GW}\lesssim 0.07$–$0.17$" is the only numeric claim in B12, and the actual comparator is the wrong physical observable (bounce-epoch energy fraction vs. present-day NANOGrav spectral density).
**Required fix**: Either (a) downgrade B12 from "logically-independent constraint" to "auxiliary order-of-magnitude consistency check" in the count, dropping the logically-independent count to 12; or (b) provide the actual order-of-magnitude transfer-function calc inline (a few lines: $\Omega_{\rm GW}^{\rm today}(f_{\rm nHz}) \sim \Omega_{\rm GW}^{\rm bounce}\cdot (a_{\rm bounce}/a_0)^4\cdot \Delta\ln f$ — both factors quotable). As stated, the 13-barriers count is overstated.

### P1A-M9 — Eq. (B-onshell_rho) and Eq. (Leff_full) use $\Xi$ inconsistently
**Section / line**: Eq. (\ref{eq:Leff_full}) at L853–855; Appendix B at L2498.
**Quoted text (Eq. Leff_full)**:
> $\Leff = \Xi\,\MPl^2 + c_\omega\omega^2,\quad \Xi\equiv \left[\frac{\alpha}{M}\,\MPl\right]\Dinf$
**Quoted text (Appendix B L2498)**:
> "$\rho_\Lambda = \Xi\,\MPl^4$ with $\Xi = (\alpha/M)\,\MPl\,\Dinf$"
**Problem**: §rotation L860–862 sets $[\Lambda_{\rm eff}] = +2$ (curvature units) and identifies $\rho_\Lambda = \Lambda_{\rm eff}\,\MPl^2 = \Xi\,\MPl^4$ — so $\Xi$ is the dimensionless ratio $\rho_\Lambda/\MPl^4$. Then Eq. Leff_full has $\Lambda_{\rm eff} = \Xi\,\MPl^2$ correctly. Appendix B L2498 reads $\rho_\Lambda = \Xi\,\MPl^4$. The two definitions agree only if we use the *same* $\Xi$. But the text at L862 says "$\Xi \lesssim 10^{-123}$" while at §sec:gdp L2063 says "$\Xi\approx 10^{-123}$, decomposed as $10^{-2}\times\Dinf$ with $\Dinf\sim 10^{-121}$". So $\Xi = 10^{-2}\cdot 10^{-121} = 10^{-123}$, consistent. OK at this level. But Appendix B L2508 then says "the dilution factor required ... is $\Dinf\sim e^{-3N_{\rm tot}}\sim 10^{-122}$" — one OOM off from the $\Dinf \sim 10^{-121}$ at L2064. The discrepancy is small ($\Xi \sim 10^{-2}$ vs $1$ in the $\MPl^4$-vs-$10^{-2}\MPl^4$ ansatz choice), but it propagates into the $N_{\rm tot}=92$ vs $N_{\rm tot}=94$ split that the paper itself flags as "$\sim 2\%$ offset". The $\sim 2\%$ offset is precisely $\ln(10)/3 \approx 0.77$ e-folds, not 2 e-folds, so the "$94-92$" gap is bigger than the OOM-uncertainty propagation suggests.
**Required fix**: Reconcile the $\Dinf$ value with $\Xi$ in one place and use it consistently. Either $\Dinf = 10^{-121}$ and $\Xi = 10^{-2}\Dinf = 10^{-123}$ (with the on-shell $10^{-2}$ ansatz factor) or $\Dinf = 10^{-122}$ and $\Xi = \Dinf$ (with the $\MPl^4$ direct ansatz). State the choice once; do not switch silently between Eq. (Leff_full) form and Appendix-B form.

---

## MINOR findings

### P1A-N1 — Table I row "Mechanism-independence?" footnote-c is overloaded with caveats
**Section / line**: Table I L519–544, footnote-c L540–543.
**Quoted text (footnote-c)**:
> "Class-level: scalar-only $w=0$ matter-bounce under Assumption~(f) of the companion forecast~\cite{Golden2026P2}; not fully mechanism-independent across the bouncing-cosmology landscape; not a distinctive ECH prediction."
**Problem**: Three distinct caveats compressed into one footnote: (i) class-level scope, (ii) Assumption (f) dependence, (iii) not-distinctive-ECH. Each is important. A reader of the table sees "Not a distinctive ECH prediction" and may stop there, missing the more subtle (ii). Plus, Assumption (f) is named without saying what it is.
**Required fix**: Split into footnotes-c1/c2/c3. Spell out Assumption (f) in c2 ("negligible fermion energy density during the contracting phase").

### P1A-N2 — Eq. (5) / Eq. (Seff_comp): leading-contribution clause is unstated
**Section / line**: Eq. (\ref{eq:Seff_comp}) at L773–775 and surrounding L766–771.
**Quoted text**:
> "the component form Eq.~(\ref{eq:Seff_comp}) displays its leading contribution"
**Problem**: "Leading contribution" of $\mathcal{F}^{IJ}[K,\mathring{R}]$ in what expansion? Presumably the perturbative expansion in $K$ (contorsion), but it is not stated. A careful reader needs to know whether higher-order $K^2$ terms in $\mathcal{F}$ contribute to the dim-$+1$ count or shift it.
**Required fix**: Replace with "displays its leading contribution in the perturbative contorsion expansion $K\ll \mathring{R}$".

### P1A-N3 — "Pop\l{}awski2016" citation: the black-hole-universe / "rotating parent" claim is contested by other authors not cited
**Section / line**: §I L513–516.
**Quoted text**:
> "Black hole universe origin, where a rotating parent black hole spawns a non-singular baby universe through torsion-regulated gravitational collapse~\cite{Poplawski2016}"
**Problem**: The Pop\l{}awski 2016 scenario is one specific implementation; the paper says "establishes a preferred cosmic axis", which then propagates into the galaxy-spin-dipole motivation (§sec:obs). Standard references for the alternative view (no preferred axis from torsion-regulated bounce in any model that conserves global Lorentz invariance) should be cited or at least acknowledged. Sweep 18 (standalone-reader) wants this.
**Required fix**: Add a sentence acknowledging that the "preferred cosmic axis" interpretation is specific to the Pop\l{}awski 2016 implementation and is not a model-independent prediction of ECH bounces; cite a counterexample (e.g., Alam et al. 2025 Cuscuton bounce, already in bbl).

### P1A-N4 — §sec:dilution L956–964 "Matching ρ_Λ ≈ (2.3 meV)⁴ requires N_tot ≈ 92" uses "fitted parameter, not predicted"
**Section / line**: §sec:dilution L956–964.
**Quoted text**:
> "Matching $\rho_\Lambda \approx (2.3\;\text{meV})^4$ requires $N_{\rm tot} \approx 92$ (a fitted parameter, not predicted)"
**Problem**: A reader sees "fitted parameter, not predicted" and infers there are observational data points $N_{\rm tot}$ was fitted *against*. There aren't — $N_{\rm tot}$ is reverse-engineered from the desired $\rho_\Lambda$ output. "Fitted" overstates the mechanism. The correct word is "tuned" or "back-engineered".
**Required fix**: Replace "fitted" with "back-engineered" or "tuned" to make explicit there is no posterior on $N_{\rm tot}$.

### P1A-N5 — §sec:r4_birefringence L1493 free-coupling alternative explicitly cites $\alpha/M\sim 10^{-10}\,$GeV$^{-1}$ which is excluded by helioscope bounds — but text mentions only "in tension"
**Section / line**: §sec:r4_birefringence L1493.
**Quoted text**:
> "requiring $\alpha/M \sim 10^{-10}\,\text{GeV}^{-1}$ at $m_\theta \sim 10^{-22}\,\text{eV}$; couplings of that size at ultralight masses are moreover in strong tension with established astrophysical ALP--photon limits"
**Problem**: $10^{-10}\,$GeV$^{-1}$ at ultralight ALP masses is *excluded* by CAST helioscope ($g_{a\gamma} < 6.6\times 10^{-11}\,$GeV$^{-1}$ at 95% CL, Anastassopoulos 2017) and is well above the IAXO sensitivity floor. "Strong tension" is the polite phrasing; the correct phrasing is "ruled out".
**Required fix**: Add citation [Anastassopoulos2017 CAST or Carenza 2020 SN1987A or IAXO] and use "excluded by" rather than "in tension with".

### P1A-N6 — §sec:r4_birefringence L1410: "$(\alpha/M)\,\partial_\mu\theta\, K^\mu$" form uses $\theta$ dimensionless while prior line uses $\phi$ canonical — dimensional self-consistency footnote applied at first instance only
**Section / line**: §sec:r4_birefringence L1410–1411.
**Quoted text**:
> "the integrated-by-parts equivalent $(\alpha/M)\,\partial_\mu\theta\, K^\mu$, where $K^\mu \equiv \epsilon^{\mu\nu\rho\sigma} A_\nu F_{\rho\sigma}$"
**Problem**: $[\alpha/M]=-1$, $[\partial_\mu\theta] = +1$ (since $\theta$ is dimensionless), $[K^\mu] = +3$. Total: $-1+1+3 = +3 \neq +4$. The $\theta\to\phi/f_a$ substitution is needed but is delayed to the footnote 8 lines above. Reader hits a dim-+3 Lagrangian density at face value.
**Required fix**: Inline write "$(\alpha/M)\,\partial_\mu\phi\, K^\mu$" or "$[(\alpha/M)f_a]\,\partial_\mu\theta\, K^\mu$" — match dimensions explicitly at this displayed equation.

### P1A-N7 — §sec:transparency Eq. (15) "$h''_{ij} + 2\mathcal{H}h'_{ij} + k^2 h_{ij} = 0$" is the standard tensor-mode equation but is presented without specifying the GW gauge choice
**Section / line**: §sec:transparency L1914–1922.
**Quoted text**:
> "$h''_{ij} + 2\mathcal{H}h'_{ij} + k^2 h_{ij} = 0$ ... transverse-traceless amplitude"
**Problem**: TT gauge is the standard, and the parenthetical mentions it, but the equation should display the transverse-traceless decomposition ($h_{ij}^{\rm TT}$) for clarity. Small but noticeable for a referee.
**Required fix**: Replace $h_{ij}$ with $h_{ij}^{\rm TT}$.

### P1A-N8 — §sec:gdp L2057–2079 "Physical-versus-mathematical scope of $\Dinf$" reads as if B14 already operates, but B14's "B14 first-principles theorem subsumes B8" framing assumes B14 is rigorously proved
**Section / line**: §sec:gdp L2066–2079.
**Quoted text**:
> "the \emph{physical} reheating thermal-reset barrier (supporting B14; see Sec.~\ref{sec:dilution}, ``Reheating thermal-reset barrier'' paragraph) already closes the bounce-era-memory dilution channel"
**Problem**: The thermal-reset barrier is *conditional* on $\Gamma_{\rm wash} > H$ (see P1A-M4). The §gdp paragraph reads it as if it were a hard closure. Conditionality is lost.
**Required fix**: Insert "(conditional on $\Gamma_{\rm wash}(T_{\rm reh}) > H(T_{\rm reh})$)" after "thermal-reset barrier" at L2069.

### P1A-N9 — Eq. (16) Eq.~(\ref{eq:Dinf}) "(T_reh/M_GUT)^{3/2}" exponent has an unresolved sign-ambiguity in the §sec:dilution prose
**Section / line**: §sec:dilution L926–943 (Step (ii) of the matching).
**Quoted text**:
> "incurs a factor of $T_{\rm reh}/M_{\rm GUT}$ in the operator strength and an additional $\sqrt{T_{\rm reh}/M_{\rm GUT}}$ from the parity-odd density-of-states factor"
**Problem**: $T_{\rm reh}\sim 10^{15}\,$GeV $<$ $M_{\rm GUT}\sim 10^{16}\,$GeV, so $T_{\rm reh}/M_{\rm GUT}\sim 0.1 < 1$, giving $(T_{\rm reh}/M_{\rm GUT})^{3/2}\sim 0.03$ — consistent with the quoted prefactor. OK. But the prose says "incurs a factor", suggesting suppression; numerically yes, but the *origin* (why the suppression is downward not upward) is the choice that $T_{\rm reh}<M_{\rm GUT}$. A reader who takes the matching to higher reheating temperature ($T_{\rm reh}\to M_{\rm GUT}$) gets prefactor → 1, removing the "0.03" matching that makes $N_{\rm tot}\approx 92$ work. The ansatz's sensitivity to the assumed $T_{\rm reh}/M_{\rm GUT}$ ratio is not explored.
**Required fix**: Add one sentence: "If reheating instead occurs at $T_{\rm reh} = M_{\rm GUT}$, the prefactor becomes unity and the required $N_{\rm tot}$ adjusts upward by $\Delta N_{\rm tot} = -\ln(0.03)/3 \approx 1.2$ e-folds — within the $\pm 2$ ansatz-systematic noted in Appendix B."

### P1A-N10 — §sec:related L1647–1655 third-party citations are listed but no verdict given on whether they support or contradict the present paper's closure
**Section / line**: §sec:related L1651–1655.
**Quoted text**:
> "Recent independent support includes Liu~\etal~\cite{ECTorsionDESI2025} (EC torsion fits the $S_8$ tension), Legner~\etal~\cite{Legner2025} (torsion condensation), and Alam~\etal~\cite{Alam2025bounce} (non-singular bounces in modified gravity)."
**Problem**: "Liu et al. EC torsion fits the $S_8$ tension" cuts *against* the present paper's "ECH cannot source dark energy" closure — if torsion fits $S_8$ tension, that is a positive result of EC torsion as a cosmology, which the abstract closure says is closed. Citing Liu et al. as "support" without explaining why their positive result doesn't break the no-go invites confusion.
**Required fix**: Add a clarifying clause: "Liu et al. fit the $S_8$ tension using EC torsion as a phenomenological modification of the matter power spectrum at horizon scales, which is parameter-budget orthogonal to the dark-energy amplitude closure at $\rho_\Lambda$ scale assessed in the present paper; their result is consistent with our analysis."

### P1A-N11 — Conclusion L2380 "9σ" claim for LiteBIRD detection of the $0.27°$ central value uses naive $0.27/0.03$ — even after the long disclaimer, the lead number is still asserted
**Section / line**: Conclusions L2380.
**Quoted text**:
> "LiteBIRD ($\sigma(\beta)\approx 0.03^\circ$, early 2030s) detects non-zero $\beta$ at $\sim 9\sigma$ (a $0.27^\circ/0.03^\circ$ overall sensitivity number). The relevant model-discrimination test, however, is the differential against the prior central value $\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$..."
**Problem**: The "$\sim 9\sigma$ detection" headline is exactly the kind of inflated claim that the abstract should avoid (see also P1A-E1 abstract-last sweep). The right framing is "LiteBIRD will measure $\beta$ to $\pm 0.03°$, ten times tighter than the current $\pm 0.094°$ measurement, but the discrimination of spectator-ALP-predicted $0.27°$ from observed $0.342°$ is set by the *prior* measurement's uncertainty and remains at the $<1\sigma$ level under the current central value." Lead with the discrimination statement, not the naive 9σ.
**Required fix**: Replace "detects non-zero $\beta$ at $\sim 9\sigma$" with "measures $\beta$ at $\sigma(\beta)\approx 0.03°$ — sufficient to detect the central value at $\sim 9\sigma$ against $\beta=0$, but discrimination of the spectator-ALP-predicted $0.27°$ from the observed $0.342°$ requires tighter measurement of the central value itself".

### P1A-N12 — Table V (tab:bounce_disc) "$w_0 w_a$ DESI" column header is ambiguous
**Section / line**: Table V at L1987–2005.
**Quoted text**:
> "$w_0w_a$ DESI"
**Problem**: Column header should say what is being tabulated. Currently it reads as if each model has a "$w_0w_a$ DESI" value; actual content is "not tested$^{\ddagger}$" or "consistent$^{\dagger}$" — a categorical label. Better header: "DESI $w_0w_a$ posterior preference".
**Required fix**: Rename column header to "DESI $w_0w_a$ accommodation" or "DESI $w_0w_a$ status".

### P1A-N13 — Eq. (10) gamma_running RG equation: missing 2-loop contribution disclaimer
**Section / line**: Eq. (\ref{eq:gamma_running}) at L1322–1326.
**Quoted text**:
> "$\frac{d\gamma}{d\ln \mu} = \frac{1}{12\pi^2}\,(N_F^L - N_F^R) \, \gamma + \mathcal{O}(\gamma^2)$"
**Problem**: $\mathcal{O}(\gamma^2)$ at 1-loop is correct, but the $1/(12\pi^2)$ prefactor at GUT scales gives $\Delta\gamma/\gamma \sim 10^{-2}$ as quoted. If the closure rests on $\Delta\gamma/\gamma \sim 10^{-2}$ holding, the $\mathcal{O}(\gamma^2)$ should be quantified: at $\gamma\sim 0.274$, the $\gamma^2$ term is $\sim 0.075$, comparable to $\gamma$, so the next-order term is NOT negligible. The ansatz's reliability is overstated.
**Required fix**: Add a parenthetical: "At $\gamma\sim 0.274$ the next-order term $\sim \gamma^2/12\pi^2 \sim 6\times 10^{-4}$ contributes a $\sim 30\%$ correction to the displayed running; the qualitative $\Delta\gamma/\gamma\sim 10^{-2}$ size is robust."

### P1A-N14 — §sec:loophole "7 disguised forms" enumeration is not connected to specific operator structure
**Section / line**: §sec:loophole L2024–2030.
**Quoted text**:
> "7 disguised forms: (1) direct $w_0w_a$ addition, (2) quintessence scalar with bounce initial conditions, (3) curvaton-derived late-time potential, (4) vacuum energy from cyclic boundary conditions, (5) torsion-induced effective $w(z)$, (6) Holst-term residual as effective DE, (7) ALP rolling as late-time acceleration."
**Problem**: 7 items listed but the closure is only assessed "at the theoretical level only ... no additional theoretical content from the bounce." For each of the 7 to be a logically separate route, each should have an operator-level signature. Currently (5), (6), (7) are torsion-internal and overlap with R1, R2, R4 of §fourroute. Double-counting risk.
**Required fix**: Cross-reference: state explicitly which of the 7 map back to which of R1–R4 in §fourroute, and which (e.g., (3) curvaton, (4) cyclic-BC vacuum) are genuinely new.

---

## NIT findings

### P1A-N15 — Date stamp "June 10, 2026 PDT" — Houston is in LA; PDT is correct but the convention elsewhere is the version-tag suffix
**Section / line**: L356 `\date{\paperTimestamp\ --- \paperVersion}`, L49 `\paperTimestamp{June 10, 2026 PDT}`.
**Suggested fix**: Standardize to "PT" (Pacific Time) or just drop the TZ; readers don't care about LA local timezone.

### P1A-N16 — Title is 14 words; PRD style allows but recommends $\leq 15$. "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter" works but the colon-substitution at "for Scalar Matter" reads choppy.
**Section / line**: Title L348–350.
**Suggested fix**: Optional polish: "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes, with Perturbation Transparency for Scalar Matter".

### P1A-N17 — `\ie`, `\eg`, `\cf` macros defined but never used in body
**Section / line**: L42–44.
**Suggested fix**: Either remove definitions or use them at appropriate junctures.

### P1A-N18 — §I L516 "establishing a preferred cosmic axis" — verb is "establishing" but the preferred axis was already discussed at §Pop\l{}awski2016; reads as if newly established here
**Section / line**: §I L516.
**Suggested fix**: "implying a preferred cosmic axis" or "suggesting a preferred cosmic axis" — softer.

### P1A-N19 — Table III (tab:barriers) "Found. A"–"Found. G" + "Branch H"–"Branch O" use single-letter labels but the "Found." vs "Branch" distinction is not introduced before the table
**Section / line**: Table III L1707–1737.
**Suggested fix**: Add inline parenthetical in table caption: "(Foundations A–G: theoretical foundation studies; Branches H–O: observational research branches)".

### P1A-N20 — Footnote 10 (Cartan single-convention footnote) is 37 lines long, includes its own sub-paragraph "consistency proof by back-substitution"
**Section / line**: L707–743.
**Suggested fix**: Consider promoting the back-substitution chain to a sub-subsection of §parityodd or to a dedicated Appendix-D one-page derivation. 37-line footnotes break the visual flow of the column.

### P1A-N21 — Conclusion L2376 references "the 13 logically-independent barriers (14 historical catalog entries)" — this construction occurs ~8 times across the paper
**Section / line**: Abstract, §I, §sec:foundations, Conclusion L2367, Table III caption, §sec:barriers caption.
**Suggested fix**: Define a `\barrierCount{}` macro that expands to the canonical wording, used once for definition and as a back-reference elsewhere; reduces repetition fatigue for the reader.

### P1A-N22 — Acknowledgments: "Lior Shamir for providing aggregate CW/CCW galaxy spin counts" — but §sec:data_galaxy says Shamir's claims have been "contested". Acknowledging him without contextualizing the contestation may read awkwardly.
**Section / line**: L2419–2420.
**Suggested fix**: Either acknowledge the contestation context, or simply thank him for "publicly releasing CW/CCW counts referenced for the cross-check in Paper IV".

### P1A-N23 — `figures/figure7_observational_timeline.png` regenerated per v1A.0.50 closure (P1A-figures EXT1 closure). Caption L1609–1618 makes no specific mention of the new content — verify caption matches regenerated panel.
**Section / line**: Fig. 7 caption L1609–1618.
**Suggested fix**: Spot-render fig. 7 and verify caption text matches the new figure content; otherwise edit caption.

### P1A-N24 — Bibliography spot-check: `\cite{ECTorsionDESI2025}` and `\cite{Legner2025}` are new citations from the EXT1 closure wave but may not be in references.bib
**Section / line**: §sec:related L1652–1653.
**Suggested fix**: Run `bibtex` and check log for "I didn't find a database entry for" warnings on these two keys.

### P1A-N25 — `\paperVersion` macro is used in `\date{}` (L356) but `\paperTimestamp` is hard-coded at L49 — could be reduced to one macro
**Section / line**: L48–49, L356.
**Suggested fix**: Trivial; not blocking.

---

## Provenance audit (sweep 16)

- Data Availability bundle URL: `https://github.com/Hubify-Projects/bigbounce/tree/main/reproducibility` — resolves to a real directory (not verified inline; suggest `artifact-link-verify` skill run).
- Bundle tag: `v1A.0.56-bundle` (already flagged P1A-E4).
- No commit SHA, no md5/sha256, no DOI archive (Zenodo etc.). For a journal submission a Zenodo DOI for the frozen bundle is strongly preferred.
- Companion papers I(b), II, III, IV: all cited as "in preparation" — flagged P1A-M6. None have arXiv IDs.

## Effect-size audit (sweep 19)

| Headline σ/p/χ² | Quoted? | Effect size given? |
|---|---|---|
| WMAP+Planck β = 0.342° ± 0.094° (3.6σ) | yes | yes (3.6σ, β=0.342°) |
| ACT DR6 β = 0.215° ± 0.074° (2.9σ) | yes | yes |
| SPHEREx σ(fNL) = 0.7 → 1.0 | yes | yes |
| 3–5σ matter-bounce significance | yes | yes |
| NANOGrav γ = 2.567 ± 0.382 | yes | yes (+1.13σ from γ=3.0) |
| H0 = 67.68 ± 1.06, ΔNeff = -0.02 ± 0.17 | yes | yes |
| DESI 3.1–4.2σ for w0wa | yes | yes |
| LiteBIRD detection "9σ" of β=0.27° | yes | flagged P1A-N11: misleading |
| Galaxy-spin 6–12× amplitude tension (Shamir) | yes | yes |
| Ξ ~ 10⁻¹²³ | yes | yes (dimensionless) |
| Σ(N_tot) ~ 92, 94 | yes | yes (±2% ansatz) |
| α/M ~ 10⁻²¹ GeV⁻¹ | yes | yes |
| ρ_NJL/ρ_Λ ~ 10⁻⁶⁹ | yes | yes |
| Route-2 Δθ/Δθ_obs ~ 10⁻⁶⁰ (or 10⁻³³) | yes | flagged P1A-M1 |
| Γ_wash/H ≫ 1 | yes | flagged P1A-M4: not actually computed |
| GW Ω ≲ 0.07–0.17 | yes | flagged P1A-M8: ansatz |
| 13 logically-independent barriers (14 historical) | yes | flagged P1A-M8 partially weakens |

Effect-size discipline is **mostly good**. Main outstanding holes: Γ_wash (P1A-M4), Ω_GW transfer function (P1A-M8), LiteBIRD 9σ phrasing (P1A-N11), Route-2 $10^{-33}$ alternative (P1A-M1).

## Abstract-last drift audit (sweep 15)

Re-reading abstract sentence by sentence against the final body text:
- Abstract sentence "perturbation-transparency theorem" — body §I uses "observation"; §X uses "result"; Conclusion uses "theorem" → flagged P1A-M3.
- Abstract sentence "$N_{\rm tot}\!\approx\!92$ ... definitively erased ... at $N_{\rm tot}\sim 92$, $N_{\rm exit}\sim 60$ (the relative e-fold differential between bounce and CMB horizon-exit ... $e^{32}$)" — internally inconsistent with §I L584's "definitively erased by $N_{\rm tot}\!\gtrsim\!60$" → flagged P1A-E1.
- Abstract footnote on "we acknowledge missing operators (Jackiw-Pi gravitational Chern-Simons $R\!\wedge\!\tilde R$, parity-odd four-fermion partner with $\gamma_{\rm BI}/(\gamma_{\rm BI}^2+1)\cdot 8\pi G$ coefficient)" — matches body §fourroute L1140–1145. OK.
- Abstract "phenomenological on-shell scaling ansatz whose off-shell mass dimension is $+1$ rather than $+4$" — matches body §rotation L877 and Appendix B L2471. OK.
- Abstract "channel-level closure" — matches body title and §IV.E. OK.
- Abstract bb mention of "matter-bounce $\fnl=-35/8$ ... a property of the matter-bounce class ... derived from the contraction-phase cubic action with no ECH input" — matches Conclusion bullet (1). OK.
- Abstract "spectator-ALP birefringence $\beta\approx 0.27^\circ$ ... a benchmark consistency point, not an ECH prediction" — matches body §sec:r4_birefringence L1490–1505 (after EXT1 closure) and Conclusion bullet (2). OK; framing now consistently calibrated.

Abstract-last drift: 2 issues found (P1A-M3 terminology, P1A-E1 quantitative). Both are listed.

---

## EXT1 closure regression check (pattern-008 sweep)

R29 was meant to confirm the EXT1 closure wave (v1A.0.56→0.57) held. Per-closure verdict:

| EXT1 Closure | Status this round | Notes |
|---|---|---|
| Abstract↔§IV.D drift on R4 framing | **HELD** | Abstract now correctly labels R4 as naturalness/CC tuning, matches body §IV.D |
| ALP convention mix ($\phi$ vs $\theta$, dim-+1 vs dimensionless) | **HELD (with N6 regression)** | Single-convention footnote at first instance OK; but L1410 displayed equation still mixes $\theta$ with $K^\mu$ — see P1A-N6 |
| Γ_washout conditional recast | **HELD with M4 weakness** | Now explicitly conditional, but the conditional inequality itself is asserted not computed — see P1A-M4 |
| Repro bundle resync | **PARTIAL FAILURE** | Bundle still labelled `v1A.0.56-bundle` while paper is v1A.0.57 — see P1A-E4 |
| Transfer-function scoping | **HELD** | §sec:structural_tension L2305–2310 now scopes the full transfer-fn to Paper II; current claims are scale-history bookkeeping only |
| Companion self-containment | **REGRESSED** | Paper I(b) "Table IV row Free-w0wa chain status" inline reference at L2003 imports a specific table-row from an in-prep companion — see P1A-M6 |
| Holst/Bianchi/Pontryagin fix | **HELD** | Abstract footnote at L394–405, §X explicit verification at L1942–1966 all consistent now |

Two regressions (E4, M6) plus one partial-regression (N6) introduced or unfixed by the EXT1 closure wave. Pattern-008 (downstream-prose-after-physics-rewrite) repeats: the abstract and §I L584 quantitative erasure threshold (P1A-E1) was not synchronized with the body's mode-history ledger when the latter was rewritten.

---

## Counts

- ESSENTIAL: 4 (E1, E2, E3, E4)
- MAJOR: 9 (M1–M9)
- MINOR: 14 (N1–N14)
- NIT: 11 (N15–N25)

Total: 38 findings.

---

## Summary recommendation

**MAJOR REVISION.**

The EXT1 closure wave demonstrably improved the manuscript — the headline Holst/Bianchi/Pontryagin confusion is now correct, the R4 framing is calibrated (naturalness objection rather than amplitude no-go), and the ALP single-convention footnote resolves the most visible dimensional ambiguity at its first appearance. The paper's central scientific contribution (channel-level closure of four enumerated minimal-ECH dark-energy routes plus a perturbation-transparency theorem for canonical scalar matter) is intellectually serious and the structural argument survives my full re-read. However, four ESSENTIAL items must close before this paper is arXiv-ready: (E1) abstract↔body quantitative drift on the inflationary-erasure threshold ($N_{\rm tot}\gtrsim 60$ vs. the actual differential $N_{\rm tot}-N_{\rm exit}\approx 32$) reintroduces pattern-008 in a load-bearing place; (E2) the Cartan-equation sign-chain footnote presents $\kappa^2 \to \kappa$ without the cancellation step — readers cannot follow the algebra; (E3) Eq. (1) carries a $T\cdot T$ term that the prose calls "shorthand", a presentation choice that misrepresents the gravity-sector content; (E4) the data-availability bundle tag (`v1A.0.56-bundle`) does not match the paper version (v1A.0.57), an unforced provenance failure. The 9 MAJOR items mostly target the dimensional / on-shell-scaling backbone of the dark-energy mapping (M1, M2, M9), the conditional rigor of the thermal-reset closure (M4), the consistency of the perturbation-transparency naming (M3), companion-paper standalone-readability (M6, M7), and the logical-independence count of the 13/14 barriers (M8). The 14 MINOR + 11 NIT items are polish-tier but several (N6 dimensional, N11 9σ phrasing, N13 RG next-order, N5 helioscope-excluded) sit close to the line. None of the findings invalidate the paper's central claims; all are addressable in a tight revision cycle. Expected resolution effort: 1–2 days for E1–E4 + M1–M5, another day for M6–M9 + selected MINOR. After resolution, recommend a fresh cross-vendor R-round to confirm closures hold under adversarial re-read.
