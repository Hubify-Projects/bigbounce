# Paper 1 — Grumpy PRD Reviewer Report

**Reviewer persona:** senior PRD torsion-cosmology referee, pedantic.
**Paper version:** v2.3.0 (\paperVersion), `arxiv/main.tex` 1215 lines, compile date 2026-04-17 (PDF 707 KB, 27 pp per SSOT).
**Recommendation:** minor revisions (with three blocking consistency fixes below)

---

## Headline

Paper 1 is the most mature of the four-paper program and is close to arXiv-ready. The theoretical architecture — 14 structural barriers, the perturbation-transparency theorem, the Cuscuton/ekpyrotic/inflation/matter-bounce discrimination table, and an unusually honest Claims Classification appendix — is a real contribution. The abstract is appropriately negative-leaning and does not overclaim the central science. Bibliography (105 entries in `references.bib`) resolves every `\cite{}` I sampled.

However, the paper has two classes of issues a PRD editor would stop on: (1) internal numerical inconsistencies between the abstract, Table II (`tab:verification`), the corner-plot figure caption, and the \emph{actual} frozen-chain diagnostic files on disk; (2) several stale reproducibility pointers (pinning to `v2.1.0` when the paper is `v2.3.0`). These are not science problems — they are attention-to-detail problems that reviewers will circle in red.

Everything else is minor polish. No science blockers.

---

## Major issues (blocking before arXiv upload)

### M1. Sample-count inconsistency for the full-tension chain.
The paper reports three different numbers for the same thing:

- **Abstract (L63):** "424,181 samples across three dataset combinations, two frozen."
- **Table tab:verification (L340):** full-tension "Total samples: 176,840" and Planck+BAO+SN "132,949." Sum with third combo ≈ 424,181. OK so far.
- **Corner plot caption (Fig. fig:corner_full_tension, L887) and §XIII (L882):** "119,617 post-burnin samples" for full-tension.
- **On-disk frozen diagnostic** `reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/convergence_summary.json`: `"total_samples_post_burn": 123129`, `"gelman_rubin_worst_r1": 0.00447`, `"burn_fraction": 0.3`, `n_chains=6`.

**Problems:**
(a) 176,840 (raw) vs. 119,617 (post-burnin) vs. 123,129 (on-disk post-burnin) are three different numbers for the full-tension chain. 119,617 ≠ 123,129 even after accounting for burn-in. Pick one and make every mention consistent.
(b) The paper's Table II states `Worst R̂−1 = 0.001` for full-tension, but the frozen diagnostic JSON says `0.00447`. A factor-of-~4.5 mismatch. This is the kind of thing an arXiv moderator will not catch but a PRD referee absolutely will.

**Fix:**
1. Pick the canonical post-burnin sample count for full-tension (I believe from the JSON: 123,129) and make Abstract, Table II, §XIII prose, and the corner-plot caption all agree. If 119,617 is from a different `getdist` rebuild on a different burn fraction, state the burn fraction next to the number.
2. Update Table II `Worst R̂−1` to 0.004 (matching the frozen diagnostic JSON), or point to the actual file from which 0.001 was taken. An R̂−1 of 0.001 is \emph{better} than what the pipeline actually produced; quoting a tighter number than you have is a referee-bait error.

### M2. H₀ mismatch between abstract and corner-plot.
- Abstract (L63): "$H_0 = 67.68 \pm 1.06$"
- Corner-plot caption and §XIII (L882): "$H_0 = 67.69 \pm 1.06$"
- Table II: $67.68 \pm 1.06$

67.68 vs 67.69 is a rounding-level disagreement on the same dataset. Pick one (presumably 67.68 from Table II, since the corner plot ran on 119,617 samples which is itself suspicious; see M1). Propagate.

### M3. ΔN_eff labeled inconsistently.
- Abstract and Table II: $-0.020 \pm 0.169$.
- §XIII corner-plot text (L882): $-0.019 \pm 0.169$.
- Appendix tab:claims (L1198): $-0.020 \pm 0.169$.
- SSOT status.md line 70: "$-0.020 \pm 0.169$" and line 148 (corner-plot note) says "$-0.019 \pm 0.169$."

The two values come from different chain slices (full raw vs. post-burnin getdist marginals). The paper should tell the reader that explicitly, or pick one. Mixing $-0.019$ and $-0.020$ across the same paper reads as careless.

---

## Minor issues (improve before arXiv)

1. **L407 reproducibility URL** points to "tree/v2.1.0/reproducibility". The paper is v2.3.0. Either the repo tag hasn't been bumped, or the paper is pointing to an old tag. A referee will clone this URL; if it 404s or is stale, that's a real reproducibility strike. **Fix:** pin to `v2.3.0` (or the latest tagged release), or add a footnote "tag pinned for reproducibility of the chains reported in this version." Same applies to L1032 and L1148.

2. **L299 "not derived in this work and are flagged as an open direction"** — the SSOT reports this as closed ("DONE 2026-04-17") but the replacement phrasing still reads as deferral. It is now honest (good) but awkward as prose. **Fix suggestion:** "The anisotropic low-$\ell$ component is not derived within the minimal ECH framework; the spectator-ALP channel of Sec.~\ref{sec:birefringence_check} is the only consistent route at present."

3. **L63 abstract: "SPHEREx at $4$--$6\sigma$"** without a citation. The number matches Golden:2026forecast but within the Paper 1 abstract it appears without the inline cite. Abstract line 63 should not carry the `\cite{}` macro (PRD style frowns on it), but the body in §X.1 (falsification, L452) should cite explicitly. **Fix:** check that L452 has `\cite{Golden:2026forecast}` — it currently does not explicitly. Add it.

4. **Eq. (22), L584:** the barrier-8 effective interaction is written
   $\mathcal{L}_{\rm eff} \supset \frac{3}{16}\frac{(J^5_\mu)^2}{\MPl^2}$
   whereas Eq.~\eqref{eq:4fermi} at L184 writes the four-fermion interaction with prefactor $-\frac{3\pi G_N}{2}\cdot\frac{\gamma^2}{\gamma^2+1}$ and axial-current index $J_{(A)\mu}$. The prefactor in Eq.~(22) drops the $\gamma^2/(\gamma^2+1)$ Holst factor and absorbs $G_N \to 1/\MPl^2$ with $3/16$ instead of $3\pi/2$ (factor of $8\pi$ difference). **Fix:** either show the reduction ($3\pi G_N/2 \cdot \gamma^2/(\gamma^2+1)$ with the EC-limit $\gamma^2/(\gamma^2+1)\to 1$ and $G_N = 1/(8\pi\MPl^2)$ giving $3/16\MPl^{-2}$), or cite a reference for the specific coefficient. Right now the jump between the two equations is invisible to the reader and looks like a factor error.

5. **Eq. (oneloop), L210:** the $g^2\sim 8\pi G_N M^2\,\gamma^2/(\gamma^2+1)\sim\mathcal{O}(1)$ claim. With $M\sim\sqrt{\gamma}\MPl$ (area-gap mass), $8\pi G_N M^2 = 8\pi (1/8\pi\MPl^2)\,\gamma\MPl^2 = \gamma \approx 0.27$. Multiplying by $\gamma^2/(\gamma^2+1)\approx 0.07$ gives $g^2 \sim 0.02$, not $\mathcal{O}(1)$. This is a factor-of-50 overestimate; the one-loop coupling is actually suppressed, which \emph{strengthens} the paper's point that $\alpha/M$ must be treated phenomenologically. **Fix:** either redo the estimate (probably picking $g^2\sim\gamma\approx 0.3$ if one drops the Holst factor, or $\sim 0.02$ if one keeps it), or footnote that $g^2\sim\mathcal{O}(0.1)$ is already perturbative.

6. **L225 "easily satisfied by any astrophysical black hole":** the parent mass threshold is $M_{\rm crit}\approx 10^{-3}M_\odot$. Every astrophysical black hole is $>3M_\odot$ by definition, but primordial black holes of this mass range are not guaranteed. **Fix:** change "any astrophysical black hole" to "any stellar-mass or supermassive black hole" — leaving open whether sub-stellar primordial BHs can source the scenario is the honest framing.

7. **Eq.~eq:Leff_full and context (L253, 257):** "The dark energy scale is set entirely by $\Xi \sim 10^{-123}$." In the abstract and L63 you cite $\Xi$ as the inflationary suppression factor $[(\alpha/M)\MPl]\Dinf$. But the inline Eq.~\eqref{eq:Leff_full} writes $\Leff = \Xi\MPl^2 + c_\omega\omega^2$, with dimensions of $[\text{mass}]^2$. Then $\rho_\Lambda = \Xi\MPl^4$ makes $\Xi$ dimensionless. These two usages (effective cosmological-constant parameter vs. dimensionless suppression factor) are identified in the text but only implicitly. **Fix:** state once, in a footnote or parenthesis, "We use $\Xi$ in both the mass-squared sense $\Leff = \Xi\MPl^2$ and the dimensionless sense $\rho_\Lambda = \Xi\MPl^4$; both are equivalent up to factors of $\MPl^2$ and context disambiguates."

8. **L262 Eq. eq:Dinf:** $\Dinf = \exp[-3N_{\rm tot}]\times(T_{\rm reh}/M_{\rm GUT})^{3/2}$. With $T_{\rm reh}\sim 10^{15}$ GeV and $M_{\rm GUT}\sim 10^{16}$ GeV the second factor is $\sim 0.03$, which is irrelevant against $e^{-276}$. **Fix:** either drop the second factor (it contributes negligibly) or justify keeping it pedagogically.

9. **L264-L265:** "reducing fine-tuning from $10^{120}$ to $\sim 10^5$." This is the reparameterization-not-resolution claim, acknowledged. But immediately below, L265 says "sensitivity to $\Delta N_{\rm tot} \approx 4$ $e$-folds." Where does "4 e-folds" come from? Sensitivity-scan Monte Carlo in `research/sensitivity_scan` gives $N_{\rm tot}\in [79, 95]$, a 16-e-fold window — not 4. **Fix:** either derive the 4 number (e.g., $\ln(10^5)/3\approx 3.8$, which is where it probably comes from) or change to "sensitivity to $\Delta N_{\rm tot}\approx\ln(10^5)/3\approx 4$."

10. **L282 Eq. eq:ClEB:** $C_\ell^{EB} \approx (\sin 4\beta)/2\cdot(C_\ell^{EE}-C_\ell^{BB}) \approx 2\beta(C_\ell^{EE}-C_\ell^{BB})$. First equality is correct. Second equality uses $\sin 4\beta\approx 4\beta$, giving $(\sin 4\beta)/2 \approx 2\beta$. Correct — but it's worth noting that this small-angle approximation fails at $\beta\sim 0.3^\circ \approx 5\times 10^{-3}$ rad only at the $\beta^3\sim 10^{-7}$ level, so the approximation is fine. No fix, just a nitpick confirming the equation.

11. **L291 "This coupling has not yet been derived in this work."** SSOT classifies this as "truly-blocked." That is fine as a scientific statement, but the passive-voice phrasing is weak. **Fix:** "The minimal ECH sector does not generate a photon-torsion coupling at one loop (the chiral-anomaly channel gives $g_{a\gamma}^{\rm torsion}\sim 7\times 10^{-26}\,\text{GeV}^{-1}$, ${\sim}10^5$ times too small; see Sec.~\ref{sec:conclusions}, L1012). Any observable birefringence therefore requires a spectator ALP (Sec.~\ref{sec:birefringence_check})."

12. **L414 Table tab:modelcomp:** $\ln B = +4.8$ for Spin-Torsion. Section VII Eq.~eq:Zcomb2 gives $+4.8\pm 0.5$ for "Full tension." OK. But the table shows $\ln B = -0.5$ for $w$CDM and $0.0$ for $\Lambda$CDM. A referee will ask: "how does $w$CDM, which has the same number of parameters ($k=7$) as Spin-Torsion, score $-0.5$ while Spin-Torsion scores $+4.8$?" The $\Delta\chi^2$ tells the story (1148.3 vs 1154.8, i.e., Spin-Torsion fits 6.5 better than $w$CDM), but that's just fit, not evidence. The factor-10 gap in $\ln B$ between two $k=7$ models with $\Delta\chi^2 = 6.5$ requires the prior-volume story. **Fix:** one-sentence note under the table: "The $\ln B$ difference between Spin-Torsion and $w$CDM arises from \emph{both} the $\chi^2$ improvement ($\Delta\chi^2 = 6.5$, contributing $\sim +3$ to $\ln B$) and the tighter prior on the spin-torsion parameter $\Delta\Neff$ relative to the flat prior on $w$." And — since this is a Savage-Dickey estimate from MCMC — add the estimation uncertainty.

13. **L391 Eq.~eq:beta_namaster:** "$\beta_{\rm NaMaster} = 0.264^\circ\pm 0.065^\circ$ (SNR = 4.1)." Abstract and elsewhere cite $\beta = 0.27^\circ$ as "the ALP prediction." Where does 0.27 come from? Eq.~(38) at L827 gives $\beta\approx 0.29^\circ$ for $C_{a\gamma}=8$, $\theta_i=1$, $m=2H_0$. The quoted "0.27" in abstract and paper body does not appear as a derived number anywhere; the spectator-ALP central prediction is 0.29. **Fix:** either change every mention of "0.27° ALP prediction" to "0.29°," or add a sentence explaining that 0.27° is the $C_{a\gamma}=8, \theta_i=0.96, m=2H_0$ choice that was used in the NaMaster Monte Carlo. Inconsistency between abstract, $\S\text{III}$, and body is one of the most common referee flags.

14. **L394 "This is $0.09\sigma$ from the ALP prediction ($\beta = 0.27^\circ$)":** denominator is the NaMaster error $0.065^\circ$; $(0.27-0.264)/0.065 = 0.09$. OK arithmetic. But if the ALP prediction is really $0.29^\circ$ (per Eq. 38), then $(0.29-0.264)/0.065 = 0.40\sigma$. **Fix:** aligns with (13) above — pin the ALP central prediction once.

15. **Table tab:barriers L506:** fine, but Barrier 11 and Barrier 1 form a closed loop by the paper's own admission (L633). That's 13 independent barriers, not 14. **Fix:** either argue why 11 is conceptually distinct even if it loops back to 1 (different EFT reasoning: decoupling-theorem vs. fine-tuning), or flag in the table caption that "Barriers 1 and 11 are coupled in the limit of ultralight torsion." Saying "14 independent" is strictly inaccurate.

16. **L452 "(2) SPHEREx ... $4$-$6\sigma$"** — no inline citation. **Fix:** cite Golden:2026forecast explicitly.

17. **L470 "factor-of-2 discrepancy between Cai \etal ($\fnl = -35/8$) and Li \etal ($\fnl = -35/16$)":** the physical bispectrum is claimed identical. Good. But if the physical bispectrum is identical, why does the abstract quote $-35/8$ specifically? **Fix:** add to the abstract "(following the convention of Ref.~\cite{Cai:2009fn}; the alternate convention $-35/16$ of Ref.~\cite{Li:2016xjb} gives an identical bispectrum up to permutation counting)."

18. **L918 NANOGrav spectral fit** explicitly uses "synthetic data points reconstructed from the published NANOGrav power-law fit, not the raw free-spectrum posteriors" — this is honest and good. But Bayes factors of $302$ and $8.1\times 10^4$ with synthetic data are then quoted in prose. **Fix:** move the caveat \emph{before} the numbers, and consider softening to "with this caveat, the best-fit is consistent with matter-bounce $\gamma = 3$." A Bayes factor from synthetic data is a referee red flag.

19. **Acknowledgments (L1054):** "author acknowledges the use of Claude (Anthropic) as an AI research assistant" — PRD accepts this now but increasingly requires specific disclosure (which sections? prompt records?). **Fix:** add "for literature survey, barrier-catalog structuring, LaTeX formatting, and consistency checking. All scientific claims and derivations were independently verified by the author."

20. **Labels multiply-defined at L256-257:**
    ```
    \label{eq:Leff}\label{eq:genfriedmann}\label{eq:raychaudhuri}%
    ```
    Three labels on a single equation. This is from earlier trims but leaves dangling labels in the reference network. **Fix:** grep for `\ref{eq:genfriedmann}` and `\ref{eq:raychaudhuri}` in the paper; if they're unused, delete the orphan labels. Same at L266 (eq:Lobs, eq:rhoLambda), L319 (eq:H0, eq:s8, eq:S8result, fig:tension_overview), L348 (5 labels), L431 (6 labels).

21. **L1055 acknowledgments:** "Computational resources were provided by the author." This is fine but "provided by the author" is an awkward locution for "self-funded." **Fix:** "Computational resources were self-funded by the author (RunPod H200 and H100 instances)."

22. **L1062–L1142 Appendices:** The SSOT claims "24 pages (focused version)" but the paper now has 27 pages per the latest compile. Several appendices are stubbed-out with just `\label{...}` lines (`app:notation`, `app:galaxy`, `app:joint`, `app:niehyan`, `app:rotation`, `app:errors`) and the body says "moved to supplementary material." The claims-table appendix `app:claims` references `Eq.~(\ref{eq:Az})` but `eq:Az` is only a `\label{}` on L271 inside §II.C — the equation for $A(z)$ is in inline prose, not a displayed equation. That cross-reference will render as "Eq.~(--)" or point to nothing meaningful. **Fix:** either typeset $A(z)=A_0(1+z)^{-p}e^{-qz}$ as a displayed equation with a single eq-label, or change the table entry to "Sec.~\ref{sec:spinmech}."

23. **References, cross-paper:** The SSOT claims Paper 1 cross-refs `Golden:2026anomalies` (Paper 3). `grep` of `main.tex` finds no such `\cite{}`. **Fix:** either add a cite to Paper 3 (SSOT claims Paper 3 is cited for the multi-survey anomaly sweep, but neither §III nor §VI mentions it) or correct the SSOT. I note the SSOT line 121 says "Cross-refs to Paper 2/3/4: PASS" — that is wrong for Paper 3.

---

## Nitpicks (optional polish)

1. L102 "\textbf{Yes} (from LQC, not ECH-specific)." — the bold "Yes" plus qualifying parenthetical reads like a marketing slide. Neutral style: "Yes (LQC holonomy correction, not ECH-specific)."
2. L107 footnote is 4+ lines of micro-math. Collapse to a sentence.
3. L231 $\rhoPl \equiv c^5/(\hbar G^2)$ — natural units have been stipulated ($c=\hbar=1$ at L180). Either restore units here or drop them; mixing is confusing.
4. L280 "The parity-odd effective action generates CMB polarization signatures through cosmic birefringence:" is a sentence-run-on into the next paragraph. Break.
5. L463 and L794 section headings "Related Work" and "Discussion" feel thin. The "Related Work" section is two paragraphs; fold into Introduction or expand.
6. L482 section title "Structural Barriers to First-Principles Dark Energy" — the word "Structural" is doing heavy lifting. Consider "14 Barriers Closing the Bounce-to-Dark-Energy Routes" or similar.
7. L616 "subject to radiative corrections of order $\delta m^2 \sim \MPl^2/(16\pi^2)$": should be $\sim \MPl^2$ (tree-level hierarchy), not $\MPl^2/(16\pi^2)$. The $16\pi^2$ loop factor is for gauge-boson loops, not gravity. **Pedantic fix:** use $\MPl^2$ or footnote the suppression.
8. L641 "at least $10^{17}$ in amplitude" — amplitude or power? GW detectors care about $h$ (amplitude); a factor of $10^{17}$ in $h$ means $10^{34}$ in energy density $\Omega_{\rm GW}$. Clarify.
9. L678 "verified numerically: $|\varepsilon^{\mu\nu\rho\sigma}R_{\mu\nu\rho\sigma}| < 10^{-15}$ across 1,000 random Riemann tensors." — Verifying the first Bianchi identity numerically is a tell that the paper outsources algebra to a computer. It's not wrong, but PRD referees prefer an analytic proof. **Fix:** cite any standard GR textbook (Wald, Carroll, MTW) for the Bianchi identity and move the numerical check to a footnote.
10. L693 "$\Delta v \equiv v_R - v_L = 0$ (exact)" — use \emph{identically} rather than "exact" to match physics convention.
11. L841 caveats "This birefringence prediction is \emph{independent of bounce cosmology}" — and yet the paper leans on it as the "surviving parity-violation evidence." That tension with §XIII (parity is the surviving science case) should be acknowledged: the surviving science case is NOT minimal ECH; it is ECH + spectator ALP. The distinction matters.
12. L985 "A first-principles derivation of the UV scale from spin-foam dynamics" — "first-principles derivation" is used ~8 times in the paper. Use sparingly; prefer "controlled derivation" or "non-perturbative calculation."
13. Redundant "self-falsified" at L452 — the model did not self-falsify; it \emph{narrowed} its own claims based on the MCMC update. Say "self-constrained" or "tightened its own uncertainty on the predicted $\Delta\Neff$."

---

## Things the paper gets \emph{right} (defense against a future hostile referee)

- The Claims Classification appendix (Table tab:claims) is unusual and excellent. Few torsion-cosmology papers state this cleanly. Keep it prominently.
- The perturbation-transparency theorem statement is sharp and proof is concise (L667–L693). No notational ambiguity.
- Honest acknowledgment that $\Xi$ is a "scaling ansatz, not a derivation" (L200, L257, L1139) — this will disarm the standard "but you can't derive $\Lambda$ this way" objection.
- The bounce-discrimination table (Table tab:bounce_disc) is a clean referee-facing summary that directly addresses "is this model falsifiable?"
- The data-availability section names specific files (`cobaya_full_tension.yaml`, `reproduce_cosmology.sh`, etc.) rather than hand-waving "code is available on request."

---

## Proposed new tasks for SSOT/queue.md

| Task ID | Title | Priority | Scope |
|---|---|---|---|
| `P1-PEER-REVIEW-SAMPLES-RECONCILE` | Reconcile full-tension sample count (176,840 raw vs 119,617 post-burnin vs 123,129 on-disk) across abstract, Table II, §XIII, corner-plot caption. Pick one canonical post-burnin count and propagate. | P1 | Edit `arxiv/main.tex` L63, L340, L882, fig caption; state burn fraction. |
| `P1-PEER-REVIEW-RHAT-FIX` | Fix worst-$\hat{R}-1$ in Table II: paper says 0.001 but frozen diagnostic JSON says 0.00447. | P1 | Edit `arxiv/main.tex` L341 to `0.004`. |
| `P1-PEER-REVIEW-H0-ROUND` | Fix 67.68 vs 67.69 inconsistency between abstract/Table II and corner-plot caption. | P2 | One-line edit. |
| `P1-PEER-REVIEW-DNEFF-ROUND` | Fix $-0.019$ vs $-0.020$ for $\Delta\Neff$ across abstract, Table II, corner-plot, tab:claims. | P2 | One-line edit. |
| `P1-PEER-REVIEW-REPO-TAG` | Update reproducibility URL pins from `v2.1.0` to `v2.3.0` (or latest tag) at L407, L1032, L1148. | P2 | Tag repo, update URLs. |
| `P1-PEER-REVIEW-ALP-027-029` | Reconcile ALP central prediction: text says "0.27°" repeatedly, Eq. (38) yields 0.29°. | P2 | Audit every mention of "0.27" vs "0.29"; pin central value. |
| `P1-PEER-REVIEW-BARRIER8-COEFF` | Clarify coefficient reduction from Eq. (eq:4fermi) $3\pi G_N/2$ to Eq. (L584) $3/16$. | P2 | Add derivation footnote. |
| `P1-PEER-REVIEW-ONELOOP-COUPLING` | Fix $g^2\sim\mathcal{O}(1)$ estimate: actually $g^2\sim\gamma\approx 0.3$ or $\sim 0.02$ with Holst factor. | P2 | L210 one-line fix + footnote. |
| `P1-PEER-REVIEW-SPHEREX-CITE` | Add `\cite{Golden:2026forecast}` to falsification §X at L452. | P3 | One-line. |
| `P1-PEER-REVIEW-PAPER3-CROSSREF` | SSOT claims Paper 1 cites `Golden:2026anomalies`; grep shows it does not. Either add cite or fix SSOT. | P3 | One-line. |
| `P1-PEER-REVIEW-ORPHAN-LABELS` | Audit multiply-defined labels at L256, L266, L319, L348, L431 — delete orphans. | P3 | Grep + clean. |
| `P1-PEER-REVIEW-NANOGRAV-CAVEAT` | Move "synthetic data points" caveat before the Bayes factors at L918. | P3 | Reorder prose. |
| `P1-PEER-REVIEW-BARRIER-COUNT` | Address whether "14 independent barriers" is strictly accurate given Barriers 1 and 11 form a loop (L633). | P3 | Caption note or prose update. |
| `P1-PEER-REVIEW-AI-ACK` | Strengthen AI acknowledgment (L1054) with specifics per PRD current policy. | P3 | 1-sentence. |
| `P1-PEER-REVIEW-EQ-AZ` | Typeset $A(z) = A_0(1+z)^{-p}e^{-qz}$ as a display equation with a proper label, remove orphan `eq:Az` label. | P3 | Edit `sec:spinmech`. |

---

## Verdict

Paper 1 is \textbf{95\% of the way to PRD-acceptable submission quality} and \textbf{98\% of the way to arXiv-acceptable.} The central theoretical contribution (14 barriers + perturbation-transparency + bounce discrimination table) is sharp, defensible, and honestly circumscribed by the Claims Classification appendix. No science blockers.

The remaining 2-5\% is a discipline problem, not a science problem: three sample-count/convergence numbers that disagree with their own on-disk diagnostic, a handful of "0.27 vs 0.29" inconsistencies on the ALP central value, and a reproducibility URL pinned to a stale tag. A PRD referee will circle these in red pen and send back to the authors for a short revision cycle. Two days of careful editing closes all of them.

\emph{Recommendation: minor revisions. Fix M1/M2/M3 before arXiv upload; handle the rest in the first PRD referee cycle. Do not submit as-is without the full-tension convergence number and sample count reconciled — that specific inconsistency is the single thing most likely to get bounced.}
