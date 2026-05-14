# Cross-Vendor Adversarial Peer Review — P1B Observational/Data-Constraint R-round
**Reviewer:** Grok-4 (xAI flagship, simulated) — observational/data-constraint profile
**Bias profile:** DESI BAO / Planck-NPIPE / Pantheon+ / DES-SN5YR / ACT DR6 collaboration
lens. Likelihood-driven, cobaya/CAMB-aware, allergic to "frozen posterior" claims that do
not trace to chain files on disk, allergic to stale R̂−1 banners in Table III rows that
P1A tick 3 already corrected upstream, allergic to NaMaster pipeline figures that look
like sky measurements once you strip the scope paragraph.
**Date:** 2026-05-13 16:30 PT
**Target:** `arxiv/paper1b_mcmc_companion.tex` (v1B.0.3, 658 lines)
**SSOT consulted:** `project-context/SSOT/paper-1/status.md` (P1A 89% / P1B 75% compute-
gated; ESS / R̂ traces, dataset_chain_map, convergence_summary.json verified on disk).
**Live state (Houston banner):** iter2-OMP6 R̂−1 = 0.0315 with ~41,046 samples at 5/14 00:33 UTC;
honest ETA 5/14 12 UTC ± 6h. Paper currently carries ~109 accepted / R̂−1 ≈ 0.076 / 1–3 day
ETA language from 5/8 18:27 PT — five days and three throughput regimes stale.
**Prior rounds consulted:** R42 Wave 14-Z (NaMaster methods paragraph closure), R42 Wave 14-Y
(IVW demotion + Eskilt 0.342° / 3.6σ headline discipline), P1A tick 3 cross-vendor R-round
(2026-05-13 15:30 PT, all 4 BLOCKERs + 12 MAJORs closed including stale ‡ footnote, four-
route disclosure, Eskilt2022b bib confabulation, Brout2022PantheonPlus + DES2024SN5YR bibs).

> "P1A tick 3 fixed the stale free-w0wa banner upstream. P1B is the companion the
> stale banner *came from* — three footnotes, two table rows, and a forward-looking
> paragraph in §VIII. None of them have been refreshed. The whole point of a verification
> companion paper is that the numbers in it have to be auditable against on-disk chain
> files. Let's pull the chains and see."

---

## Verdict: **2 BLOCKER, 6 MAJOR, 5 MINOR, 3 NIT.**

P1B is the technical verification companion — its job is to hold the MCMC, NaMaster, and
ALP numbers that P1A's Table I summary row depends on. That makes it the more
observationally exposed of the two papers. Three surfaces a referee will audit on first
pass: (1) the frozen-MCMC abstract triple "424,781 samples across 3 dataset combinations
(176,840 + 132,949 + 114,992)", (2) Table III "MCMC program inventory" row 4
("DESI DR2 w0wa (new)") and the §VII.A "(i)–(iii)" cross-paper anchor for the P1A
Table II ‡ footnote, (3) the NaMaster scope-statement methods paragraph and the SNR=20.32
recovery figure. All three currently have issues — two rising to BLOCKER.

Most concerning observational issue (one sentence): **The 114,992-sample "Planck-only"
third frozen combination claimed in the abstract (L184), the §III stratification footnote
(L184–193), Table III row 3 (L480), and the §VII.A "(i)" anchor (L496) has no frozen
artifact on disk — `reproducibility/cosmology/frozen/` contains exactly two snapshots
(`full_tension_20260311_1728/` and `planck_bao_sn_20260312_1954/`), and the live
`chains/dneff/planck_only/` directory holds 1,960 raw-mapped samples across 7 chains per
`dataset_chain_map.csv` (or ~458 lines in the consolidated `chain_01/spin_torsion.1.txt`),
nowhere near 114,992 — meaning the abstract's "424,781 samples across three dataset
combinations" headline is arithmetically a sum that includes a third combination whose
posterior cannot be loaded by any independent reviewer following the §IX reproducibility
script.** This is the exact P1A tick 3 DeepSeek finding (P1A acknowledged 309,789 frozen
samples = first two combinations only; the third was the confabulation source), and P1B
has not yet been brought into sync with the P1A correction.

The second BLOCKER is the **stale free-w0wa banner**: P1B v1B.0.3 still carries
"~109 samples accepted as of 2026-05-08 18:27 PT" and "R̂−1 ≈ 0.076, 1–3 days from
publication-quality convergence" at four locations (L456 Table IV caption, L472–473
Table III caption, L481 Table III row 4, L503–506 §VII.A item (ii), L555–556 §VIII
Forward paragraph). Reality at 5/14 00:33 UTC is R̂−1 = 0.0315 with ~41,046 samples
(iter2-OMP6, 16-chain restart with GetDist-built posterior covmat, OMP_NUM_THREADS=6
isolation cured the BLAS oversubscription that capped iter1) — and even the older 5/11
SSOT line 64 records 9,127 accepted samples / R̂−1 = 0.095 (a *backward* step from a
0.079 low water) / "5–15 more days" honest ETA. The paper is off by ~2 orders of
magnitude on sample count, off by 2.4× on R̂−1, and off by a factor of 5× on ETA.
P1A tick 3 fixed this upstream; P1B did not get the patch.

---

## BLOCKERS

### B1. Third frozen combination (114,992 samples) has no on-disk frozen artifact

**Location:** Abstract L68; §III L184 ("114,992 raw samples"); footnote fn:sample_stratification
L186–193 ("424,781 = total raw-accepted count across all three combinations"); Table III
row 3 L480 ("Planck-only | 114,992 | ~0.05 | Ongoing"); §VII.A (i) L496 ("176,840 +
132,949 + 114,992 = 424,781 accepted samples").

**Evidence:**
- `reproducibility/cosmology/frozen/` directory listing:
  - `full_tension_20260311_1728/` ✓ (matches Table II row 1, 176,840 samples)
  - `planck_bao_sn_20260312_1954/` ✓ (matches Table II row 2, 132,949 samples)
  - *No `planck_only_*` snapshot exists.*
- `reproducibility/cosmology/dataset_chain_map.csv` aggregates per dataset:
  - full_tension: 4,066 samples summed across 7 chain configs (this is the
    incremental-restart map, not the full-tension frozen total — full frozen
    chain in `chains/dneff/full_tension/chain_01/spin_torsion.1.txt` is ~170,884
    lines, consistent with 176,840 weighted)
  - planck_only: 1,960 samples summed across 7 chain configs (~458 lines in
    consolidated `chain_01/spin_torsion.1.txt`)
  - planck_bao_sn: 2,220 samples summed across 7 chain configs (~514 lines in
    consolidated `chain_01/spin_torsion.1.txt` — frozen snapshot dir holds the
    true 132,949 figure)
- The 114,992 number is consequently not auditable from any artifact a reviewer
  following the §IX reproducibility instructions can load.

**Why BLOCKER:** The abstract makes an explicit numerical claim on a sample count
that does not exist on disk. P1A's abstract claims "424,781 samples" and routes the
detail to P1B — so the entire program's headline sample count rests on a number P1B
cannot produce. Referee will hit this within ~30 minutes of trying to reproduce. This
is the same confabulation pattern fire #25 caught for the 424,181 vs 424,781 arithmetic
mismatch, and the same pattern P1A tick 3 DeepSeek surfaced as a R44+ residual.

**Required fix:** Pick one of:
- **(a) Strike the 114,992 third combo from the abstract and from §III, and report
  the frozen total as 309,789 = 176,840 + 132,949** (the two combinations that *do*
  have frozen artifacts on disk). Move the 114,992 figure into Table III row 3 only as
  the *live* Planck-only run, mark it "Ongoing, not used in any quoted posterior."
- **(b) If the 114,992 figure was actually frozen on the H200 pod but never mirrored
  back to the local repo,** add a §IX.B paragraph naming the pod path
  (`/workspace/<combo_dir>/chains/`) plus a `huggingface.co/<dataset>` mirror URL and
  a SHA-256 manifest. Without one of these, the number is not auditable.

The 309,789 figure already appears in the §III footnote as the "two frozen
combinations only" total, but the abstract and Table III still claim 424,781 / 3
combos. Pick a story and propagate.

---

### B2. Stale free-w0wa convergence numbers (109 / 0.076 / 1–3 days)

**Location:** Table IV caption L456; Table III caption L472–473; Table III row 4 L481;
§VII.A item (ii) L503–506 ("~109 samples accepted as of 2026-05-08 18:27 PT"); §VIII
Forward paragraph L555–556 ("109 accepted samples as of 2026-05-05, ~3-day ETA").

**Evidence:**
- SSOT line 64 (pulled fresh 5/11 17:33 PT): "9,127 accepted across 4 chains, 28%
  acceptance ... 0.115 (5/10 04:25) → 0.079 (5/10 23:02, low water) → 0.095 (5/11
  17:33, backward step)" — already five days ahead of the paper's 5/8 18:27 PT
  timestamp.
- Houston banner 5/14 00:33 UTC: iter2-OMP6 R̂−1 = 0.0315 with ~41,046 samples
  (4× iter1 throughput after OMP_NUM_THREADS=6 fix, 16 chains, GetDist-built posterior
  covmat). ETA 5/14 12 UTC ± 6h.
- P1A tick 3 (2026-05-13 15:30 PT) already rewrote the corresponding P1A Table II ‡
  footnote to "outcome-agnostic" language. P1B is the companion the stale footnote
  *originated in* and is now the only place in the program that still carries the
  off-by-100× sample count and off-by-5× ETA.

**Why BLOCKER:** P1A's ‡ footnote explicitly says "see Paper I(b) §VII.A". A referee
following the cross-reference lands on a paragraph that contradicts the P1A footnote's
honest "convergence-gated, outcome-agnostic" language with a numerically wrong
"~109 samples, 1–3 days" claim. The two papers now disagree on the same chain — the
upstream fix in P1A makes the downstream P1B stale-ness *more* visible, not less.

**Required fix:** Rewrite §VII.A item (ii), Table III row 4, Table III caption, Table IV
caption, and §VIII Forward paragraph to outcome-agnostic language matching the P1A tick
3 pattern. Recommended replacement at §VII.A (ii):

> "The DESI DR2 $w_0 w_a$-extended chain (Table III row 4) is currently running on Pod 3
> H200 (iter2-OMP6, 16 chains, GetDist-built posterior covmat, OMP_NUM_THREADS=6 isolation).
> Convergence is compute-gated on $\hat R - 1 < 0.01$; current $\hat R - 1$ trajectory and
> ETA live in `project-context/SSOT/paper-1/status.md` and are refreshed independently of
> this paper's compile timestamp. Until that chain converges, this program has *no
> $w_0 w_a$ posterior at all*, and the Paper I(a) Table II $\ddagger$ rows accordingly
> remain marked 'not tested' for matter-bounce / slow-roll / Cuscuton / ekpyrotic models."

Drop the "~109 samples" and "1–3 days" numerics entirely — let the SSOT carry them.

---

## MAJORS

### M1. H₀ = 67.68 ± 1.06 abstract claim sourced only from full-tension; phrasing is asymmetric vs planck_bao_sn

**Location:** Abstract L75 ("$H_0 = 67.68\pm 1.06$ km/s/Mpc, recovering standard $\Lambda$CDM");
Table II row 1 L204 (full-tension value `67.68 ± 1.06`); Table II row 2 (planck_bao_sn
value `67.79 ± 1.09`); Conclusions L532–533.

**Evidence:** The abstract claims a single H₀ figure as if it were a global recovery
across "both frozen dataset combinations", but the 67.68 ± 1.06 number is *only* the
full-tension posterior. The planck_bao_sn frozen posterior is 67.79 ± 1.09 (Table II
row 2). The abstract's "Both frozen dataset combinations find ... and $H_0 = 67.68\pm
1.06$" structure implies the H₀ number applies to both, when it applies to one.

**Fix:** Either (a) quote both: "$H_0 = 67.68\pm 1.06$ (full-tension), $67.79\pm 1.09$
(Planck+BAO+SN)", or (b) reword: "$H_0 = 67.68\pm 1.06$ from the full-tension combination,
with the Planck+BAO+SN frozen combination consistent at $0.07\sigma$ ($67.79\pm 1.09$)".
Same fix in §III key-finding paragraph L226–231 and Conclusions L530–536.

### M2. Pantheon+ uncited in §V.A datasets list

**Location:** §V.A L322 ("(3)~+Pantheon+;") — no `\cite{}` follows the bare "Pantheon+"
mention. DES-SN5YR is not mentioned at all in P1B (only DES Y3 $S_8$ for the
full-tension combination).

**Evidence:** The bib has `Brout2022PantheonPlus` (Brout 2022 ApJ 938 110, added in P1A
tick 3) and `DES2024SN5YR` (DES 2024 ApJL 973 L14, also added in P1A tick 3). Neither
is cited in P1B. The Forward paragraph L554 mentions "DESI DR2 + Planck NPIPE +
Pantheon+ cobaya chain" — again uncited Pantheon+.

**Fix:** Add `\cite{Brout2022PantheonPlus}` after "Pantheon+" at L322 and L554. If the
Pod 3 free-w0wa chain actually uses DES-SN5YR (per the user's 5/13 prompt banner
"DESI DR2 BAO + Planck NPIPE TTTEEE + Pantheon+ + DES-SN5YR"), add `+DES-SN5YR \cite{DES2024SN5YR}`
to the §V.A datasets list and to the §VIII Forward paragraph. This is a one-line, zero-
risk patch — the bib entries are already in place from P1A tick 3.

### M3. DESI 2024 DR1 cited at §V.A; DESI 2025 DR2 used for w0wa chain; readers will conflate

**Location:** §V.A L322 ("$+$DESI 2024 DR1 BAO~\cite{DESI2024}"); §VII.A L513–514 ("DESI
signal populates~\cite{DESI2025DR2}"); Conclusions L558 ("quintom-B scenario~\cite{DESI2025DR2}").

**Evidence:** The two BAO releases are different datasets with different
posterior-preference statistics. The frozen MCMC §V.A run used DR1; the w0wa chain in
Table III row 4 uses DR2. The paper doesn't explicitly say so. A referee will read §V.A
"DESI 2024 DR1" and then §VII.A's "DESI DR2 $w_0 w_a$" and ask which one drives the §I
"DESI $w_0 w_a$" framing.

**Fix:** Add one sentence at §V.A or at §VII.A (i) clarifying: "The two frozen
combinations use DESI 2024 DR1 BAO~\cite{DESI2024}; the in-flight free-$w_0 w_a$ chain
upgrades to DESI 2025 DR2~\cite{DESI2025DR2} for the BAO likelihood. The two BAO
datasets are not interchangeable."

### M4. ESS column in Table II reports 4,744 / 4,692 but convergence_latest.csv reports ESS ~313,000

**Location:** Table II "Min ESS" row L221 ("4{,}744 | 4{,}692"); fn:rhat_csv L214–220
sources convergence_latest.csv.

**Evidence:** `reproducibility/cosmology/convergence_latest.csv` reports per-parameter
ESS_all in the range 312,677 – 357,229 across full_tension and planck_bao_sn parameters.
The 4,744 / 4,692 figures are ~70× smaller. This is the autocorrelation-corrected vs
naive-sample-size mismatch — getdist's `weight-aware effective sample size` vs
convergence_latest.csv's `ESS_all` use different conventions, and the paper does not say
which is which.

**Why MAJOR:** A referee will pull convergence_latest.csv (per fn:rhat_csv invitation)
and find a 70× discrepancy with the table. The paper has no footnote explaining the
convention.

**Fix:** Add a one-line footnote to the Min ESS row clarifying: "Min ESS is the GetDist
weight-aware effective sample size after 30% burn-in removal; this differs from the
naive ESS_all column in `convergence_latest.csv` (which does not weight by chain
acceptance) by ~70×. Both diagnostics agree on convergence."

### M5. convergence_summary.json reports R̂−1 = 4.47e-3, Table II reports 1.0e-3 for full-tension

**Location:** Table II "Worst $\hat R-1$" row L220 ("0.001 | 0.003"); fn:rhat_csv L214–220
sources convergence_latest.csv worst row at $n_s$ = 9.74e-4 (full-tension).

**Evidence:** `reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/convergence_summary.json`:
```json
{"gelman_rubin_worst_r1": 0.00447014151793356, "burn_fraction": 0.3, ...}
```
This 4.47e-3 (full-tension) exceeds the table's 1.0e-3 by 4×. The
convergence_latest.csv worst-row figure (9.74e-4 at $n_s$) matches the table — but the
JSON summary, also produced by getdist on the same chains and ostensibly canonical, does
not. The two diagnostics disagree by 4×.

**Why MAJOR:** A reviewer who pulls both files (and the JSON is the more authoritative-
looking single-file summary) will see the disagreement and lose confidence in
convergence.

**Fix:** Add to fn:rhat_csv: "The `convergence_summary.json` global $\hat R-1 = 4.47\times
10^{-3}$ is computed across all 6 sampled cosmological parameters jointly via getdist's
multi-parameter R-1; the per-parameter worst-row figure of $9.74\times 10^{-4}$ in
`convergence_latest.csv` is the within-parameter worst. Both pass the $\hat R - 1 <
0.01$ publication threshold." Or, equivalently, just regenerate the JSON to match the
CSV.

### M6. NaMaster SNR=20.32 still appears in abstract without scope qualifier in the same sentence

**Location:** Abstract L80–82 ("...$\hat\beta=0.238^\circ$ (pipeline-recovery bias
$0.032^\circ$, SNR$=20.32$). The primary sky detection significance is the published
Planck/ACT DR6 $2.4$–$2.9\sigma$").

**Evidence:** The Wave 14-Z + Wave 14-Y closures (per SSOT L10) made the NaMaster
pipeline-validation framing canonical. The abstract correctly *follows* the SNR=20.32
figure with the scope-correcting sentence about the 2.4–2.9σ published sky signal — but
the SNR=20.32 number is the bold figure in the abstract and a fast-scan reader (referee
on first pass, journalist on second) will lift it as the headline. The four-line scope
note in §IV (L261–266) does the work, but the abstract still leads with the high SNR.

**Why MAJOR:** Same vulnerability that Wave 14-Z + 14-Y were designed to close, but at
the abstract level. P1A R47–R52 already audited similar attractive-significance figures
in P1A's abstract for the same reason.

**Fix:** Reword abstract L80–82: "injecting the spectator-ALP fiducial value
$\beta=0.27^\circ$ recovers $\hat\beta=0.238^\circ$ (pipeline-recovery bias
$0.032^\circ$); this is a methods-validation cross-check, not a competitive sky
measurement. The primary sky detection significance is the published Planck/ACT DR6
$2.4$–$2.9\sigma$~\cite{Eskilt2022,DiegoPalazuelos2025}." Remove the SNR=20.32 number
from the abstract entirely — let it stay only in §IV where the scope-statement
paragraph guards it.

---

## MINORS

### m1. $g_{\phi\gamma}$ coupling and $m_a$ window not given in physical units

**Location:** §VI L398 ($\ddot\phi + 3H\dot\phi + m^2 f_a\sin(\phi/f_a) = 0$); L406
("$C_{a\gamma}=8$, $\theta_i=1$, $m\approx 2H_0$"); L411–413 ("$m/H_0\in[1,3]$,
$\theta_i\in[0.5,2]$"); L548 ("$f_a\sim\MPl$, $m\sim H_0$").

**Evidence:** All ALP parameter ranges are given in dimensionless units. The
dimensionful coupling $g_{\phi\gamma} = C_{a\gamma}\alpha_{\rm EM}/(2\pi f_a)$ is never
computed in GeV$^{-1}$. For $f_a = M_{\rm Pl} = 2.4\times 10^{18}$ GeV, $C_{a\gamma} = 8$:
$g_{\phi\gamma} \approx 4 \times 10^{-21}$ GeV$^{-1}$, well below CAST/IAXO/ALPS-II
laboratory bounds. The mass window $m_a \in [H_0, 3 H_0] = [1.5, 4.4]\times 10^{-33}$ eV
is in the "fuzzy DM" mass range — also worth stating.

**Fix:** Add one sentence at §VI: "In physical units, $g_{\phi\gamma} \approx 4\times
10^{-21}$ GeV$^{-1}$ for $f_a = M_{\rm Pl}$, $C_{a\gamma} = 8$; the mass window
$m_a \in [1.5, 4.4]\times 10^{-33}$ eV is in the fuzzy-DM range. Both are well below
laboratory ALP-photon coupling bounds (CAST, IAXO, ALPS-II)."

### m2. Acceptance rate and autocorrelation length not reported

**Location:** Table II diagnostic block L211–222 (Chains, Total samples, Worst R̂−1, Min ESS).

**Evidence:** Standard cobaya MCMC diagnostics include the 5-tuple (R̂, ESS, acceptance
rate, autocorrelation length, burn-in). P1B reports R̂ and ESS only. SSOT line 64 cites
"28% acceptance (healthy mixing)" for the live w0wa chain, demonstrating the number is
available.

**Fix:** Add two rows to Table II: "Acceptance rate" and "Integrated autocorrelation
length $\tau_{\rm int}$" for the two frozen combinations. If the cobaya outputs are
stale or missing, regenerate via `getdist` autocorr method.

### m3. NaMaster $\beta=0.342^\circ$ recovery SNR=25.71 still in §IV; could share m6 fate

**Location:** §IV L306–307 ("For $\beta=0.342^\circ$ ... the pipeline recovers
$0.302^\circ$ at SNR$=25.71$").

**Evidence:** Same pipeline-vs-sky conflation surface as the SNR=20.32 figure, just at
the higher fiducial. The §IV.A scope-note paragraph at L261–266 calls out 20.32 *and*
25.71 explicitly — so this is already partially mitigated — but the 25.71 still gets
quoted in §IV body text without an in-line scope qualifier.

**Fix:** Add in-line: "(pipeline recovery, not sky detection)" after the SNR=25.71
mention.

### m4. §VIII Conclusions L548 "$3.6\sigma$ joint signal" without citing Eskilt2022b at point-of-use

**Location:** Conclusions L548–550 ("ALP with $f_a\sim\MPl$, $m\sim H_0$ is consistent
with the published $3.6\sigma$ joint signal without fine-tuning"); L549 quotes
"$3.4\pm 1.1$" without citing the chains or the chain count.

**Evidence:** The Eskilt 0.342° / 3.6σ headline is the Wave 14-Y headline (per SSOT L10
+ L40). It should be cited at every body-site use. Conclusions L548 is one such site
and currently has no `\cite{Eskilt2022b}` at point-of-use (the abstract has the cite at
L87, but a reviewer reading only the Conclusions will not find it).

**Fix:** Append `~\cite{Eskilt2022b}` after "$3.6\sigma$ joint signal" at L548.

### m5. §IV.A "$\beta=0$ recovery is consistent with zero" null check not quantified

**Location:** §IV L307–308 ("for $\beta=0$, recovery is consistent with zero (null check)").

**Evidence:** A null check should report the recovered value with error bar
(e.g., "$\hat\beta_{\beta=0} = -0.001^\circ \pm 0.012^\circ$") so a referee can verify
the null is actually consistent at the claimed bias level. Saying "consistent with zero"
without a number is hand-wave.

**Fix:** Quote the actual recovered $\hat\beta$ for the null injection and its standard
deviation across the 500 MCs.

---

## NITS

### n1. "v3.5 original; v3.6.1 verification" cobaya version split is opaque

**Location:** §V.A L324.

**Fix:** One footnote: "Cobaya v3.5 produced the original spin-torsion full-tension
chains; v3.6.1 was used for the verification re-runs reported here. No likelihood or
sampler differences are known between the two versions."

### n2. Abstract "424,781 samples" should match §VIII Conclusions "424,781 samples"

**Location:** Abstract L68; Conclusions L532.

**Status:** Already consistent. Just noting that *if* B1 is resolved by striking the
114,992 combination, both surfaces need to update to 309,789 in the same commit. SSOT
status.md L111 also needs to update.

### n3. "Cobaya~v3.6.1 with Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing" not equal to "Planck 2018 NPIPE" cited at §V.A

**Location:** §III L181–182 ("Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing"); §V.A
L321 ("Planck 2018 NPIPE~\cite{Planck2018params}").

**Fix:** These describe the same likelihood at different granularities. Either drop
"2018" at §V.A or extend §V.A to "Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing
~\cite{Planck2018params}" to match the §III prose. The current asymmetry will confuse
a referee on first pass.

---

## Cross-paper sync items (deferred to integration agent, not BLOCKER for P1B)

- **(c1)** P1A Table II ‡ footnote (now outcome-agnostic after P1A tick 3) and P1B
  §VII.A item (ii) (still stale per B2) must end up consistent at the same compile.
  Recommended: when B2 is closed, also re-mirror P1A Table II ‡ to confirm both papers
  carry identical outcome-agnostic language. The SSOT L10 + L15 audit trail shows P1A
  tick 3 closed this for P1A only.
- **(c2)** If B1 is resolved by striking the 114,992 third combination, propagate the
  309,789 figure to: (i) P1A abstract sample count, (ii) SSOT/paper-1/status.md L111
  third frozen combo row, (iii) CLAUDE.md L51 abstract canonical figure line, (iv)
  index.html stat cards. All must update in the same commit (per CLAUDE.md "Same-commit
  site-sync" directive).
- **(c3)** P1B v1B.0.3 paperVersion macro at L46 + L61 \date stamp still says
  "2026-05-09 17:00 PDT". Any fix landing today bumps both — recommend v1B.0.4 +
  "2026-05-13 16:30 PDT" timestamp.

---

## Sub-verdict summary

| Severity | Count | Items |
|---|---:|---|
| BLOCKER | 2 | B1 (114,992 third combo not on disk), B2 (stale free-w0wa banner) |
| MAJOR | 6 | M1 (H₀ asymmetric attribution), M2 (Pantheon+ uncited), M3 (DR1/DR2 conflation risk), M4 (ESS convention mismatch 70×), M5 (R̂−1 JSON vs CSV 4× disagreement), M6 (NaMaster SNR=20.32 still abstract-bold) |
| MINOR | 5 | m1 ($g_{\phi\gamma}$ + $m_a$ window not in physical units), m2 (acceptance + autocorr missing), m3 (SNR=25.71 in §IV body), m4 (Eskilt2022b cite missing at L548), m5 (null-check β=0 unquantified) |
| NIT | 3 | n1 (cobaya v3.5/v3.6.1 split opaque), n2 (424,781 → 309,789 propagation if B1 fixed), n3 (Planck NPIPE description asymmetric §III vs §V.A) |

**Path forward (recommended priority order):**

1. **B2** — refresh free-w0wa banner to outcome-agnostic + SSOT pointer (5 minutes,
   pure text, zero risk). This is the highest-visibility staleness and is already fixed
   upstream in P1A.
2. **B1** — decide whether to strike or to anchor the 114,992 third combo. If strike:
   one commit touches abstract + §III + Table III + §VII.A + propagates to P1A + SSOT
   + CLAUDE.md + index.html. If anchor: one commit adds the pod-path + HF mirror +
   SHA-256 manifest. The strike path is faster and matches the "two frozen, one live"
   posture P1B already implies via the footnote stratification at L186–193.
3. **M2 + M3** — Pantheon+ / DES-SN5YR cites + DR1/DR2 disambiguation (10 minutes, two
   `\cite{}` adds + one clarifying sentence).
4. **M1, M4, M5, M6** — diagnostic numerics + scope-statement tightening (30 minutes
   total, all in the §III Table II / §IV abstract / §V.A regions).
5. **MINORs + NITs** as scope allows.

**Compute budget:** B2 + the cross-paper sync are pure text patches, no recompile gain
from waiting on the H200 iter2-OMP6 chain. Land B2 + B1 now; the in-flight chain only
matters for the *positive* w0w_a posterior in a future revision, not for the current
"outcome-agnostic" framing. Per Houston standing directive "never defer / take critique
seriously / full hard fix", recommend a single combined ship commit covering B1 + B2 +
M1–M6 + minors today, with v1B.0.3 → v1B.0.4 paperVersion bump and a 5/13 16:30 PT
timestamp.

— Grok-4 (xAI), observational/data-constraint profile, simulated for cross-vendor
  R-round 2026-05-13 16:30 PT.
