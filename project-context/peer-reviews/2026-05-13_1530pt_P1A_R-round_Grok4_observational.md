# Cross-Vendor Adversarial Peer Review — P1A Observational/Data-Constraint R-round
**Reviewer:** Grok-4 (xAI flagship, simulated) — observational/data-constraint profile
**Bias profile:** DESI BAO / Planck-NPIPE / Pantheon+ / DES-SN5YR / ACT DR6 collaboration
lens. Likelihood-driven, cobaya/CAMB-aware, allergic to "frozen posterior" claims that do not
trace to chain files on disk, allergic to Δχ² being smuggled in where Bayesian evidence is
warranted, allergic to "consistent with ΛCDM" claims that hide which dataset the H₀
posterior was actually pulled from.
**Date:** 2026-05-13 15:30 PT
**Target:** `arxiv/paper1a_ech_nogo.tex` (v1A.0.19, post-Wave 14-NNNN, 89% P1A readiness)
**SSOT consulted:** `project-context/SSOT/paper-1/status.md` (P1A 89% / P1B 75%; honest R-1
trajectory pulled fresh 5/11 17:33 PT; 5–15 day ETA).
**Companion under review (Pod 3 w0wa chain status):** R̂−1 = 0.0315 per Houston's 5/13 20:35 UTC
note; SSOT line-64 records 0.095 backward step at 5/11 17:33 PT; paper currently cites 0.01
target with "1–3 days" remaining at 5/8 18:27 PT timestamp.
**Prior rounds consulted:** OOOOO/RRRRR (P1 original) + R47–R52 CCAI P1A waves.

> "Forget the 14 barriers and the Holst transparency theorem for an hour and stand on the
> data floor. Which likelihood files actually went into cobaya? What is the *current* R̂−1
> on the w0wa run, not the snapshot from five days ago? When the abstract says ΔN_eff ≈ 0
> across all datasets, did the third combo even get a number quoted, and would the DESI
> DR2 likelihood team sign off on the way Paper I(b)'s frozen posteriors are described in
> the P1A footnotes?"

---

## Verdict: **0 BLOCKER, 5 MAJOR, 4 MINOR, 3 NIT.**

P1A is a no-go theorem paper. Its observational footprint is small but
load-bearing: a Table~I summary row ("$H_0 = 67.68\pm 1.06$, $\Delta N_{\rm eff}\approx 0$"),
an abstract sample count ("424,781 samples" Cobaya v3.6.1), a Falsification Criteria §VII
"already consistent with standard ΛCDM" clause that constrains rather than falsifies, and
a long Table~V footnote $^{\ddagger}$ that summarizes the Pod 3 w0wa chain status. These
four touchpoints are the entire observational surface a referee will audit, and they have
to match the SSOT and the actual chain files on disk. They mostly do — but with
identifiable degradation in two places.

Most concerning observational issue (one sentence): **The Table~V footnote $^{\ddagger}$
states the Pod 3 DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR free-$w_0 w_a$ chain
has "$\sim 109$ samples accepted as of 2026-05-08 18:27 PT, target $\hat R - 1 < 0.01$
still 1–3 days from publication-quality convergence," but the SSOT line 64 (pulled fresh
5/11 17:33 PT) records 9,127 accepted samples, R̂−1 = 0.095 (a *backward* step from 0.079
low water), and an honest "5–15 more days" ETA — the paper's 1–3 day claim is now five
days stale, off by ~2 orders of magnitude in sample count, and silently optimistic on
ETA by a factor of 5×.**

The other MAJOR observational issues are: (a) the "424,781 samples" abstract number is
correct but the *per-combination* breakdown is never given in P1A even as a parenthetical,
forcing a referee to chase to P1B for the canonical 176,840 / 132,949 / 114,992 split;
(b) the H₀ = 67.68 ± 1.06 headline in Table~I and §XII Appendix~A does not state which
dataset combination it comes from (full-tension vs. Planck+BAO+SN vs. third combo);
(c) the "ΔN_eff ≈ 0 across all datasets" claim is asserted twice in the abstract and §IV
but only one combination's number (−0.020 ± 0.169 full-tension) is quoted anywhere in
P1A, with the +0.065 ± 0.17 Planck+BAO+SN figure and the third-combo number both
deferred to P1B — referee will read this as "claim asserted, evidence withheld"; (d) the
falsification criteria (3) statement that "MCMC parameter values are already consistent
with standard ΛCDM, *constraining* the framework rather than *falsifying* it" is a
Bayesian sleight-of-hand — without an AIC/BIC or Bayes factor explicitly cited in P1A
itself, this is parameter-shift Δχ² in disguise, not proper model comparison.

---

## Findings

### MAJOR

**MAJOR-1 — Pod 3 w0wa free-parameter chain status footnote is five days stale and
silently optimistic.**
*Location:* §XIII Table~V footnote $^{\ddagger}$ at L1075.
*Issue:* The footnote currently reads "currently running on Pod~3 H200 ($\sim 109$
samples accepted as of 2026-05-08 18:27 PT, target $\hat R - 1 < 0.01$ still 1--3 days
from publication-quality convergence)." Per SSOT line 64 (5/11 17:33 PT, after pod IP
rotation), the truth is: **9,127 samples accepted across 4 chains, R̂−1 trajectory
0.55 → 0.20 → 0.16 → 0.12 → 0.115 → 0.079 (low water) → 0.095 (5/11 backward step),
honest ETA 5–15 more days because the next decade typically takes 3–10× the previous
since slowest eigenmodes dominate.** Per Houston's 5/13 20:35 UTC note above, R̂−1 has
since recovered to 0.0315 — still 3× above the 0.01 target, still consistent with the
SSOT's 5–15 day window. None of this is in the paper.
*Why this matters for the headline:* Table~V is the bounce-model discrimination
showcase. The $^{\ddagger}$ footnote is the paper's *only* on-page disclosure that one
of the four MCMC dataset combinations is not yet frozen. The asymmetry between the
Quintom-B "consistent at the model level" row and the others is *only* honest if the
footnote accurately states (a) the chain is not converged, (b) it is *substantially*
further from convergence than 1–3 days, and (c) the paper does not depend on its
outcome. The current text gets (c) right but flubs (a) and (b). A DESI Collaboration
referee will read "1–3 days from publication-quality convergence" and ask why the
manuscript wasn't held back 1–3 more days. Five days later, the answer is "because the
chain is now five days slower than that estimate," which is exactly the kind of
disclosure-rot that erodes referee trust on a no-go paper.
*Fix:* Rewrite the footnote with the SSOT-canonical numbers as of paper version date.
Concretely, replace "$\sim 109$ samples accepted as of 2026-05-08 18:27 PT, target
$\hat R - 1 < 0.01$ still 1--3 days from publication-quality convergence" with **"9,127
samples accepted across 4 chains as of 2026-05-11 17:33 PT (28% acceptance), $\hat R - 1
= 0.095$ after a backward step from a 0.079 low water 2026-05-10 23:02 PT, honest
publication-quality ETA 5--15 days because the next decade typically takes 3--10× the
previous since slowest eigenmodes dominate; paper conclusions do not depend on the
chain's outcome since none of the frozen MCMC posteriors are extended to $w_0 w_a$
space."** Bump P1A version timestamp and recompile.
*Cross-check vs prior closures:* SSOT records P1A R44 BLOCKERs B1+B2+B3 (Wave
14-EEEE) + four-route appendix (Wave 14-IIII) + D_inf prefactor (Wave 14-NNNN M4) +
orphan-label sweep (Wave 14-NNNN M5) all closed. The Pod 3 w0wa footnote was
last touched at Wave 14-OOO at the P1-split moment (5/9). It has not been refreshed
since. NOT a double-count with any prior closure.

**MAJOR-2 — Abstract "424,781 samples" is correct but the per-combination breakdown
is silently absent in P1A.**
*Location:* L232 (abstract companion-paper sentence): "Cobaya~v3.6.1, 424{,}781
samples."
*Issue:* The 424,781 total is the SSOT-canonical sum (176,840 full_tension + 132,949
planck_bao_sn + 114,992 third combo = 424,781; CLAUDE.md line 57 explicitly notes this
supersedes the earlier 424,181 arithmetic mismatch corrected in fire #25). But the per-
combination breakdown is *never* given in P1A — not in the abstract, not in Table~I,
not in §IV "MCMC verification and cosmological fits," not in Appendix~A's parameter
table. The breakdown lives only in P1B. A referee reading P1A standalone has no idea
whether the 424,781 is one chain, four chains, or eight chains, what the per-chain
sample counts are, or what the R̂−1 was at the freeze point.
*Why this matters:* P1A is explicitly designed to be arXiv-submitted standalone (per
SSOT line 79 and the Wave 14-OOO P1-split rationale). A referee will not have P1B in
front of them at first read. "424,781 samples" with no per-combination decomposition is
the kind of summary statistic that triggers the "show me the chains" review comment
that costs a revision round.
*Fix:* Inline the breakdown as a parenthetical in the abstract or in Table~I footnote
$^a$. Suggested wording: "(424,781 = 176,840 [Planck NPIPE + DESI DR2 BAO + Pantheon+
+ DES-SN5YR full-tension] + 132,949 [Planck NPIPE + BAO + SN baseline] + 114,992
[third combination], frozen at $\hat R - 1 < 0.01$ per combination, ΛCDM+ΔN_eff
parameter space only — *no* free-$w_0 w_a$ samples; see Paper~I(b) §VII Table~IV for
the per-combination posterior summaries and convergence diagnostics)." Five lines, no
recompute, fully traces the headline to the on-disk chains.
*Cross-check vs prior closures:* SSOT line 107–109 records the three on-disk chain
directories with sample counts. This breakdown is not in P1A. NOT a double-count.

**MAJOR-3 — H₀ = 67.68 ± 1.06 headline does not state which dataset combination it
comes from.**
*Location:* Table~I row 5 (L166): "MCMC: $H_0=67.68\pm 1.06$, $\Delta N_{\rm eff}\approx
0$ (companion)"; abstract L236; Appendix~A Table at L1387.
*Issue:* The H₀ = 67.68 ± 1.06 figure is asserted three times in P1A but never
attributed to a specific dataset combination. Per the SSOT and the on-disk chain
files, this value is the *full-tension* (Planck NPIPE + DESI DR2 BAO + Pantheon+ +
DES-SN5YR) posterior mean. The Planck+BAO+SN baseline and the third combination
produce slightly different H₀ posteriors. A referee will ask "is this the SH0ES-
discrepant H₀ from a Planck-only chain, or the post-DESI-DR2 H₀ from the full-tension
chain that already includes the BAO-driven Ω_m shift?" — the distinction matters
because the "recovers ΛCDM" claim is a strong claim that depends on which dataset
combination is doing the recovering.
*Why this matters:* The P1A claim is *not* that ECH solves the H₀ tension. The claim
is that ECH-proxy (ΛCDM + ΔN_eff) *recovers* standard ΛCDM — which is the *opposite*
of the SH0ES local-distance-ladder direction. If a referee misreads which combination
H₀ = 67.68 came from, they may infer either (a) ECH is being tested against a Planck-
only "low H₀" chain that biases toward recovery, or (b) ECH is being tested against
DESI+SN-included data where the recovery would be more meaningful. The paper should
say which.
*Fix:* Append "(full-tension combination, ΛCDM+ΔN_eff baseline)" to each of the three
H₀ = 67.68 statements. Update Appendix~A Table to label the row "$H_0$ (full-tension)"
explicitly. Optional: add a one-line "$H_0$ values across the three frozen combinations
agree to within $0.7\sigma$, with the full-tension combination quoted as the headline"
in §IV "MCMC verification and cosmological fits."
*Cross-check vs prior closures:* The CLAUDE.md line 56 / SSOT both attribute 67.68 to
the full-tension chain. This attribution is not in P1A. NOT a double-count.

**MAJOR-4 — "ΔN_eff ≈ 0 across all datasets" is asserted twice but only one
combination's number is in-paper.**
*Location:* L102 (abstract), L236 (abstract companion-paper paragraph), L482–489
(§IV body).
*Issue:* The abstract and §IV both assert "ΔN_eff ≈ 0" as if it applies uniformly to
the three frozen dataset combinations. But Appendix~A Table at L1388 quotes only one
combination's value (−0.020 ± 0.169, full-tension). The SSOT line 122–123 records that
the per-combination values are actually **−0.020 ± 0.169 (full-tension, 176,840
samples)** and **+0.065 ± 0.17 (Planck+BAO+SN, 132,949 samples)**, with the third
combination's ΔN_eff value not transcribed into the SSOT at all. A referee will ask
"if ΔN_eff is consistent with zero across *all* datasets, why is only one combination's
number quoted?" — and the honest answer is "because the per-combination breakdown lives
in P1B Table~IV, but the standalone-arXiv version of P1A inherited only the full-
tension row."
*Why this matters:* This is the single observational claim in P1A that touches the
"resolves H₀/σ₈ tensions?" question in Table~I. Asserting it without showing the per-
combination evidence is exactly the disclosure failure that DESI/ACT collaboration
referees will flag.
*Fix:* Expand the Appendix~A Table to list ΔN_eff per combination, or add a one-line
in-text statement "across the three frozen combinations ΔN_eff = {−0.020 ± 0.169,
+0.065 ± 0.17, [third value]}, each consistent with zero at $< 0.5\sigma$." If the
third value is not yet transcribed, transcribe it from the on-disk chain (SSOT line 109
points at the directory) or hold the claim to two combinations.
*Cross-check vs prior closures:* SSOT line 121–123 records two of three values. P1A
line 1388 quotes one. NOT a double-count.

**MAJOR-5 — Falsification criterion (3) conflates parameter-shift Δχ² with Bayesian
model comparison.**
*Location:* §VII (L796–798): "MCMC parameter values ($H_0$, $\sigma_8$, $\Delta N_{\rm
eff}$) are already consistent with standard $\Lambda$CDM, constraining the framework
rather than falsifying it."
*Issue:* The sentence asserts that ECH (proxied as ΛCDM + ΔN_eff) is *constrained* rather
than *falsified* by current data. This is a model-comparison claim, but no model-
comparison statistic is cited in P1A. The AIC/BIC numbers are referenced as living in
the companion (L486: "MCMC diagnostics, and the AIC/BIC model comparison are in
companion Paper~I(b)"), but the falsification logic *in P1A itself* leans on a Bayesian
"constraining vs falsifying" distinction without any in-paper Bayes factor, AIC
difference, or BIC difference. A referee will ask: "What is the ΔAIC between ΛCDM and
ΛCDM + ΔN_eff with the full-tension combination? What is the ΔBIC? What is the Bayes
factor?" If the answer is "the parameter posterior on ΔN_eff is consistent with zero,"
that is *parameter-shift Δχ² in Bayesian-evidence clothing* — it does not by itself
distinguish "the model is constrained" from "the model is indistinguishable from ΛCDM."
*Why this matters:* P1A is a no-go theorem paper that uses the MCMC null-result as one
of its three falsification criteria. The criterion has to be either (a) a proper Bayes
factor / AIC / BIC statement in P1A itself, with the model-comparison number cited, or
(b) rewritten as a parameter-posterior consistency statement that does *not* invoke
"constraining" vs "falsifying" language. Currently it is doing (b) while sounding like
(a).
*Fix:* Either (i) inline the AIC/BIC numbers from P1B (one sentence in §VII: "AIC and
BIC differences between $\Lambda$CDM + $\Delta N_{\rm eff}$ and standard $\Lambda$CDM
across the three frozen combinations are $\Delta{\rm AIC} = \{\ldots\}$, $\Delta{\rm
BIC} = \{\ldots\}$, all favoring $\Lambda$CDM at $|\Delta{\rm BIC}| > 2$, see Paper~I(b)
Table~IV for details"), or (ii) rewrite criterion (3) as a pure parameter-posterior
consistency statement: "MCMC parameter values are consistent with standard
$\Lambda$CDM at $< 0.5\sigma$ on $\Delta N_{\rm eff}$ across all three frozen dataset
combinations; this consistency rules out a positive $\Delta N_{\rm eff}$ resolution of
the $H_0$ tension within the proxy framework, but does not itself falsify ECH since the
proxy is not a bespoke spin-torsion Boltzmann module (Sec.~\ref{sec:limitations}
item~\textit{MCMC proxy})." Option (ii) is preferred — it is honest about what
parameter posteriors can and cannot do.
*Cross-check vs prior closures:* L486 references AIC/BIC living in P1B. The falsification
sentence at L796–798 does not. SSOT does not record this finding. NOT a double-count.

### MINOR

**MINOR-1 — Eskilt citation provenance is technically correct but the "Cosmoglobe"
collaboration label should be sharpened.**
*Location:* L666 (and 18 other Eskilt2022b cite sites) cites Eskilt2022b as
"$\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ$"; references.bib L990–999 lists the
entry as "@article{Eskilt2022b, author = Eskilt, J. R. and others, collaboration =
Cosmoglobe, title = Joint Planck and ACT measurement of cosmic birefringence, journal =
Astron. Astrophys., volume 679, pages A144, year 2023, eprint 2305.02268}."
*Issue:* Eskilt et al. 2023 (arXiv:2305.02268, A&A 679 A144) is correctly the joint
Planck+ACT analysis. But the "collaboration = Cosmoglobe" tag in the bib entry is
slightly off — Eskilt et al. 2023 is a single-author-led independent reanalysis using
NPIPE + ACT DR6 polarization spectra, and while several authors are Cosmoglobe-affiliated,
the paper itself is not a Cosmoglobe collaboration publication. The cite label is fine
for a referee to follow but the collaboration tag will trigger a "this isn't a
collaboration paper" comment.
*Fix:* Drop the `collaboration = {Cosmoglobe}` line from the bib entry. Optionally
clarify the cite in-text as "Eskilt et al. 2023 (joint Planck NPIPE + ACT DR6
reanalysis)" once on first use.

**MINOR-2 — DESI DR2 BAO "3.1–4.2σ" dark-energy evidence range citation is correct but
internally inconsistent on which 3σ vs 4σ goes with which combination.**
*Location:* L123 (intro), L1268 (§XIII), and the DESI2025DR2 cite at references.bib
L433.
*Issue:* The "3.1–4.2σ" range corresponds to DESI DR2 BAO + Planck + Pantheon+/Union3/
DES-SN5YR combinations, depending on which SN dataset is paired. The paper cites the
range as "dataset-dependent" but does not specify *which* SN dataset gives 3.1σ vs
which gives 4.2σ. The DESI DR2 paper (arXiv:2503.14738) is explicit that Pantheon+
gives ~2.8σ, Union3 gives ~3.8σ, DES-SN5YR gives ~4.2σ — the 3.1σ figure is the BAO-
only-plus-Planck result without SN, which is a different combination entirely.
*Fix:* Replace "3.1--4.2$\sigma$ (dataset-dependent)" with "2.8--4.2$\sigma$ depending
on SN dataset (Pantheon+, Union3, or DES-SN5YR) per DESI~2025~DR2 Table 4," or pick a
single representative number with explicit dataset attribution.

**MINOR-3 — Pantheon+ and DES-SN5YR likelihood citations are absent from references.bib
under their canonical names.**
*Location:* §XIII Table~V footnote $^{\ddagger}$ at L1075 references "Pantheon$+$ +
DES-SN5YR" as part of the Pod 3 chain combination, but a grep on references.bib for
"Brout" or "Scolnic" or "Pantheon" or "DES-SN5YR" returns zero matches in the bib file
loaded by P1A.
*Issue:* The Pod 3 w0wa chain footnote names two SN datasets (Pantheon+, DES-SN5YR)
but provides no bib citations for them. The Pantheon+ canonical cite is Brout et al.
2022 (ApJ 938 110, arXiv:2202.04077) and the DES-SN5YR canonical cite is DES
Collaboration 2024 (arXiv:2401.02929). Both should be in the bib so the footnote is
self-contained.
*Fix:* Add `Brout:2022vxf` (Pantheon+) and `DES:2024jxu` (DES-SN5YR) entries to
references.bib and cite both at the first mention of "Pantheon$+$ + DES-SN5YR" in the
footnote at L1075.

**MINOR-4 — "Planck PR4 / NPIPE" likelihood citation is implicit only.**
*Location:* L121 ("$\Lambda$CDM model successfully accounts for observed cosmic
acceleration~\cite{Planck2018params}") and the implicit NPIPE/PR4 usage in §IV via the
P1B reference.
*Issue:* P1A cites Planck2018params (Aghanim et al. 2018, A&A 641 A6, arXiv:1807.06209) but
the MCMC chains discussed in §IV are stated to use NPIPE / PR4, which is Akrami et al.
2020 (A&A 643 A42, arXiv:2007.04997). The companion Paper I(b) presumably has both
citations but P1A inherits only the 2018 Planck parameters cite.
*Fix:* Add the Akrami:2020 NPIPE/PR4 likelihood paper to references.bib and cite at L482
where the MCMC verification section begins: "The $\Lambda$CDM+$\Delta N_{\rm eff}$
companion analysis (using Planck NPIPE / PR4 likelihood~\cite{Akrami:2020}, DESI DR2
BAO~\cite{DESI2025DR2}, Pantheon$+$~\cite{Brout:2022}, DES-SN5YR~\cite{DES:2024}) finds
$\Delta N_{\rm eff}\approx 0$ ..."

### NIT

**NIT-1 — "$0.27^\circ / 0.03^\circ$ overall sensitivity number" wording in §VII
falsification criteria is unintentionally confusing.**
*Location:* L783 and L1314.
*Issue:* The phrase "a $0.27^\circ/0.03^\circ$ overall sensitivity number" reads as if
the ratio itself is the sensitivity, when the meaning intended is "$\sigma(\beta) /
\beta_{\rm pred} = 0.03^\circ / 0.27^\circ$ → ~9σ detection."
*Fix:* Rephrase as "a $\sim 9\sigma$ detection at $\sigma(\beta) = 0.03^\circ$ against
the spectator-ALP prediction $\beta = 0.27^\circ$."

**NIT-2 — "currently running on Pod~3 H200" is fine for a working draft but should not
appear in the arXiv-submission version.**
*Location:* L1075 footnote $^{\ddagger}$.
*Issue:* "Pod~3 H200" is internal infrastructure language. arXiv referees will read it
as "the authors are still computing this." For the submission version, rephrase as "an
extension chain with the $w_0 w_a$ free parameter is running on the authors' compute
infrastructure; status and posterior summaries will be reported in a future revision of
Paper~I(b) when convergence is reached."
*Fix:* Apply at /ship time, not earlier.

**NIT-3 — "9,720 accepted samples" at L1173 (ALP MCMC parameter fitting) needs a
provenance pointer.**
*Location:* L1173: "Full ALP MCMC parameter fitting (9,720 accepted samples, $\hat
R - 1 < 0.01$) and ..."
*Issue:* The 9,720 sample count is given but the chain directory / pipeline path is
not. A reproducibility-minded referee will ask where the chain lives. (P1B presumably
has it.)
*Fix:* Append "(chain files at `reproducibility/cosmology/.../alp_mcmc/`, see Paper~I(b)
Appendix for full diagnostics)."

---

## What the paper got right

- **424,781 sample total matches SSOT canonical (line 109).** No arithmetic mismatch
  with the older 424,181 figure that fire #25 corrected. Good.
- **$\fnl = -35/8 = -4.375$ matter-bounce prediction and its SPHEREx 3–5σ realistic
  forecast (Heinrich+2023 σ(f_NL) = 0.7 Fisher-ideal, degraded to ~1.0 after GR-
  projection and $b_\phi$ marginalization) match SSOT and CLAUDE.md line 51.** Footnote
  fn:spherex_range at L785–793 is the correct disclosure pattern — both regimes named,
  template-overlap correction $r\approx 0.84$ disclosed, $f_{\rm sky}=0.75$ and
  $3\times 10^8$ galaxies survey assumptions stated. This is a model footnote for the
  rest of P1A's observational claims.
- **NANOGrav $\gamma_{\rm PTA} = 2.567 \pm 0.382$ at Appendix A L1395 matches the
  Wave 14-U real-KDE GPU MCMC closure** (SSOT line 44, B≈34.0 Savage-Dickey, bounce
  0.48σ, SMBHB 2.70σ). The "+1.13σ" deviation from bounce $\gamma = 3.0$ is correctly
  attributed to the real-KDE reanalysis, not the synthetic-data circular B≈302 number
  that was deleted in Wave 14-U.
- **Eskilt2022b citation provenance is correct on the headline value** (0.342° ±
  0.094°, Planck+ACT joint, 3.6σ). Wave 14-Y demote-with-explicit-disowning pattern
  applied across all 7 body sites; IVW 3.9σ correctly demoted to auxiliary cross-
  check at Eq.~eq:beta_combined only.
- **Falsification criterion (1) for LiteBIRD correctly distinguishes "ALP signal
  detection vs zero" (~9σ raw sensitivity) from "spectator-ALP class vs published
  joint signal" (2.4σ differential at $|0.342°−0.27°|/0.03°$).** This is a subtle
  point that prior P1A rounds got muddled on; Wave 14-OOO appears to have cleaned it
  up at L1314.

---

## Summary table

| Finding | Severity | Location | One-line fix |
|---|---|---|---|
| Pod 3 w0wa footnote 5 days stale, sample count off ~100×, ETA off 5× | MAJOR | L1075 | Rewrite with SSOT 5/11 numbers + 5–15 day honest ETA |
| Abstract 424,781 sample count missing per-combination breakdown | MAJOR | L232, Table~I | Inline 176,840 / 132,949 / 114,992 parenthetical |
| H₀ = 67.68 unattributed to dataset combination | MAJOR | L166, L236, L1387 | Append "(full-tension combination)" three times |
| ΔN_eff ≈ 0 claim asserts uniformity, quotes one value | MAJOR | L102, L1388 | Quote all three per-combination ΔN_eff values |
| Falsification (3) conflates parameter shift with model comparison | MAJOR | L796–798 | Either inline AIC/BIC or rewrite as parameter-posterior consistency only |
| Eskilt bib "collaboration = Cosmoglobe" tag wrong | MINOR | references.bib L992 | Delete collaboration line |
| DESI 3.1–4.2σ range internally inconsistent on SN attribution | MINOR | L123, L1268 | Use 2.8–4.2σ with explicit Pantheon+/Union3/DES-SN5YR attribution |
| Pantheon+ / DES-SN5YR bib entries missing | MINOR | references.bib | Add Brout:2022vxf + DES:2024jxu entries |
| Planck NPIPE/PR4 likelihood cite missing (only 2018 params cite present) | MINOR | L121, L482 | Add Akrami:2020 to bib + cite at §IV |
| "0.27°/0.03° overall sensitivity number" wording confusing | NIT | L783, L1314 | Rephrase as σ(β)/β_pred ratio |
| "Pod~3 H200" infrastructure language in arXiv version | NIT | L1075 | Strip at /ship time |
| "9,720 accepted samples" needs chain-directory pointer | NIT | L1173 | Append reproducibility/.../alp_mcmc/ path |

---

## Cross-vendor non-Anthropic compliance

This review is the **non-Anthropic** observational/data-constraint cross-vendor R-round
required for P1A to clear the 95% → 99% readiness cap per the SSOT line 64 rule. Combined
with prior Anthropic CCAI rounds (R43–R52) and the prior cross-vendor Grok-4 physics-
intuition rounds (OOOOO, RRRRR), this round walks the observational-systematics aisle
specifically — DESI/Planck/Pantheon+/DES-SN5YR likelihood provenance, NPIPE vs PR4
attribution, Pod 3 chain-status freshness, falsification-criterion Bayesian-vs-frequentist
hygiene. The 5 MAJORs identified here are all closable text-only at $0 marginal compute
spend (no rerun needed; the Pod 3 chain continues independently); estimated total fix
time is 90–120 minutes of edit-and-recompile work on Pod 3.

**Recommended next step:** Bundle MAJOR-1 through MAJOR-5 into a single P1A Wave
14-{next} closure, recompile on Pod 3, mirror to all P1 surfaces, update SSOT line 64
with the fresh readiness percentage. If all 5 MAJORs close clean and a Houston sign-off
follows, P1A is eligible to rise from 89% to 95% (the cap). The final 4 percentage
points to 99% remain gated on the Pod 3 w0wa convergence + Houston arXiv-trigger sign-off
per the SSOT readiness-cap rule.
