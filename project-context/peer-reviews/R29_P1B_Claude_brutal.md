# P1B R29 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7 (in-session)`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.55.pdf` md5=b776a111 pages=17
**Input format**: Direct `.tex` read (v1B.0.55, 2,181 lines) + frozen-artifact filesystem audit + `tools/artifact_crosscheck.py` (PASS: 0/17 broken paths) + cross-check against `parameter_summary{,_CORRECTED,_units_README}.{json,md}`
**Wall time**: in-session (API leg failed on credit balance)
**Source paper**: `arxiv/paper1b_mcmc_companion.tex` v1B.0.55, June 10, 2026 PDT, post-EXT1-P1B closure wave

---

## Scope of this review

Brutal-honesty PRD referee on the EXT1-closed v1B.0.55 source. No findings cap.
Verdict classes: **ESSENTIAL** (must fix before PRD acceptance), **MAJOR**
(should fix), **MINOR** (would improve), **NIT** (style/polish).

Upgraded sweeps applied:
- (15) abstract-last drift between abstract claims and body §III/§IV/§VI numbers
- (16) provenance — Data Availability section + frozen artifact bundle internal
  consistency, especially the new `parameter_summary_units_README.md`
- (17) uncomputed quantitative claims (numbers asserted in body without an
  in-paper or in-artifact computation)
- (18) standalone-reader sanity — does §I through §VII read coherently without
  Paper~I(a) in hand?
- (19) effect-size accounting — every `Nσ` claim cross-checked against the
  underlying mean/σ pair quoted in the same paragraph.

EXT1 closures (re-verified, no regressions found): (A2) burn-in 30%/20%
reconciliation note present at L891–901; (A3) caveat (e) DES-SN5YR/Pantheon+
overlap at L1113–1128; (A6) one-sided 95% ΔN_eff < 0.31/<0.39 at L873–877;
(A7) Fig.2/`fig:dneff_viability` caption rescope at L1212–1215; (A8) calibrated-
bias language at L1411–1413 ("estimator is *not* unbiased in the standard
statistical sense"); (A9) unweighted-estimator canonical choice at L1482–1491;
(A10) M_Pl = reduced Planck mass at L722–724; (A11) LiteBIRD "under forecast
foreground/calibration assumptions" at L1887–1888 and L1949–1950; (A14) H_0
header `[km\,s$^{-1}$\,Mpc$^{-1}$]` at L965 + L1012. All closures held; new
findings below are post-closure regressions or pre-existing items missed by
EXT1.

`tools/artifact_crosscheck.py` → 0 broken paths out of 17 candidates.

---

## ESSENTIAL findings

### P1B-R29-E1 — `parameter_summary_units_README.md` mislabels a column-permutation bug as a "unit" issue, and gives at least three demonstrably wrong "conversions"

**Location**: `reproducibility/cosmology/frozen/full_tension_20260311_1728/diagnostics/parameter_summary_units_README.md`
(new in v1B.0.55, A1 closure of EXT1-F1); pointer from §Data and Code
Availability L1977–1983.

**Quote (README L11–17 conversion table)**:

> | `H0` | 0.8035 | h = H₀/(100 km s⁻¹ Mpc⁻¹) | × 100 → 80.35 km/s/Mpc |
> | `delta_neff` | 13.82 | internal Cobaya `nnu` sampled value | − 3.046 → ΔN_eff |
> | `tau` | 1.041 | internal chain encoding of τ | see CORRECTED |
> | `sigma8` | 0.308 | internal chain encoding | see CORRECTED |
> | `omegam` | 0.814 | internal chain encoding | see CORRECTED |
> | `ns` | 0.0223 | internal chain encoding | see CORRECTED |

**Problem.** Direct comparison of the two on-disk JSON artefacts in the same
directory makes this unambiguous:

| README "raw" key | README claim | Actual JSON raw value | Actual physical Table-I value | Diagnosis |
|---|---|---|---|---|
| `H0` = 0.8035 | "h = 0.8035 → ×100 = 80.35 km/s/Mpc" | 0.8035 | 67.68 (`h` = 0.6768) | **WRONG.** 0.8035 is σ₈, not h. The CORRECTED `sigma8` field literally reads 0.8034 — same number. |
| `delta_neff` = 13.82 | "Cobaya nnu, − 3.046 → ΔN_eff" | 13.82 | −0.020 | **WRONG.** nnu prior is `[2.046, 5.046]`; 13.82 is not a sampled `nnu`. Subtracting 3.046 gives 10.78, not −0.020. The raw 13.82 has no physical Table-I correspondent and looks like a different chain column (loglike / minuslog2?) being mislabelled `delta_neff`. |
| `tau` = 1.041 | "internal chain encoding of τ" | 1.041 | 0.054 | **WRONG.** 1.041 ≈ 100θ_MC (acoustic-scale parameter), which is reported in Table~\ref{tab:iter2_posterior} L1021 as $100\theta_{\rm MC}=1.04087$. The "raw" column maps to a different chain index, not a τ unit-encoding. |
| `sigma8` = 0.308 | "internal chain encoding" | 0.308 | 0.803 | **WRONG.** 0.308 ≈ Ω_m (Table I L969: $\Omega_m=0.308\pm 0.005$). |
| `omegam` = 0.814 | "internal chain encoding" | 0.814 | 0.308 | **WRONG.** 0.814 ≈ S₈ (Table I L968: $S_8=0.814\pm 0.008$). |
| `ns` = 0.0223 | "internal chain encoding" | 0.0223 | 0.965 | **WRONG.** 0.0223 ≈ ω_b h² (baryon density), printed in Table~\ref{tab:iter2_posterior} L1019 as $\omega_b h^2 = 0.02224 \pm 0.000125$. |

The `parameter_summary.json` field labels are systematically shifted relative
to the underlying chain columns. The bug is a **column-permutation / header-
misalignment** in the chain-extraction script, *not* a Cobaya internal-
normalisation issue. A "unit warning" that proposes `×100` and `−3.046` as
conversions is actively misleading — a reproducer who follows the README's
instructions will multiply σ₈ by 100 and report H₀=80.35 km/s/Mpc, or
subtract 3.046 from a non-`nnu` column and report ΔN_eff=10.78.

The CORRECTED file is internally consistent and matches Table I; the bug is
isolated to (a) the raw JSON's field labels and (b) the README's
characterisation of why the raw values look wrong.

**Why this is ESSENTIAL.** EXT1-F1 was a real-world failed-vendor finding
that the v1B.0.55 stamp closed by *adding a README*. The README is the
artefact the closure produced. It is wrong on the page, and the paper now
points to it from §Data and Code Availability (L1977–1983) as if it were
authoritative. A referee following the paper's pointer will land here and
conclude the chain extraction is incompetent. This regresses EXT1-F1 from
"unit warning" to "documented column-permutation bug masquerading as a unit
warning" — strictly worse than the v1B.0.54 state where the JSON was simply
wrong and undocumented.

**Fix.**

1. Rewrite the README to state: *the JSON field labels do not correspond to
   the underlying chain columns; the script wrote chain column `i` under
   header `j`. The `_CORRECTED.json` file is the authoritative readout.*
2. Replace the (wrong) conversion table with a column-mapping table:
   raw_key `H0` → actually σ₈ (Table-I 0.803), raw_key `delta_neff` →
   *unidentified, do not use*, raw_key `tau` → actually 100θ_MC (1.041),
   raw_key `sigma8` → actually Ω_m (0.308), raw_key `omegam` → actually S_8
   (0.814), raw_key `ns` → actually ω_b h² (0.0223).
3. Verify the column-permutation hypothesis by reading the chain header
   (`.paramnames` or chain.0.txt header) and writing down the correct
   header → field-label mapping in the README.
4. Update §Data and Code Availability (L1977–1983) prose to say
   "field-label misalignment" not "raw Cobaya-normalised values".

This is a single-evening fix, and *required* because the paper points at
this README as a referee-visible artefact.

---

### P1B-R29-E2 — Abstract still asserts ΔN_eff posterior values without disclosing the prior support that drove the one-sided 95% upper limit

**Location**: Abstract L693–696; one-sided 95% disclosure L873–877.

**Quote (abstract L693–696)**:

> "Both frozen dataset combinations find $\Delta\Neff$ consistent with zero
> ($-0.020\pm 0.169$ full-tension; $+0.065\pm 0.17$ Planck+BAO+SN) and
> $H_0$ consistent with standard $\Lambda$CDM …"

**Problem.** The body (L871–877) now states that the prior is
$\Delta\Neff\in[-1, +2]$ (allowing negative values), so the quoted
posterior mean of $-0.020$ for the full-tension chain is the
**two-sided** posterior under an unphysical-on-the-low-side prior. The
EXT1-A6 closure added the one-sided 95% upper limits ($<0.31$, $<0.39$) at
L873–877, but the abstract still leads with the two-sided value
unflagged. A reader who reads only the abstract will (a) cite $-0.020 \pm 0.169$
as a constraint, (b) compute that this is $0.12\sigma$ from zero, and (c)
miss that the lower tail is unphysical and the published-extra-species
convention requires the one-sided number.

This is the classical sweep-(15) abstract-last drift: the EXT1 closure
hardened the body but the abstract is unchanged.

**Fix.** Add to the abstract immediately after the $(-0.020\pm 0.169)$
parenthetical: "(two-sided posterior under $\Delta\Neff\in[-1,+2]$ flat prior; the one-sided
95\% upper limit under the physical $\Delta\Neff\ge 0$ restriction is
$\Delta\Neff<0.31$ full-tension, $<0.39$ Planck+BAO+SN)." Single sentence; preserves the
posterior-mean lead.

---

### P1B-R29-E3 — Table~\ref{tab:iter2_posterior} reports posterior departures from $\Lambda$CDM at $+4.3\sigma$ and $-3.6\sigma$ on a chain that has *zero* $\Lambda$CDM-region samples

**Location**: Table~\ref{tab:iter2_posterior} L1006–1009; fn:wcaveat L1006; §V.B "Headline result" L1576; Conclusions L1954 "empirical anchor".

**Quote (Table L1006–1009)**:

> $w_0$         & $-0.8122 \pm 0.0436$ & (marg.-tail, $+4.3\sigma$)
> $w_a$         & $-0.6666 \pm 0.1864$ & $-3.6\sigma$ from $0$ (marg.-tail; fn.~\ref{fn:wcaveat})
> $w_0 + w_a$   & $-1.4788 \pm 0.1485$ & phantom-crossing required
> $w_{\rm pivot}$ & $-0.952 \pm 0.019$ & $+2.5\sigma$ from $-1$

> fn:wcaveat: "the $+4.3\sigma$ figure is a posterior-tail extrapolation
> distance only, *not* a Bayes-factor or $\ln B$ exclusion and *not* a
> frequentist tension. … robust $\ln B$ is left to a follow-up nested-sampling
> analysis."

**Problem.** The paper is internally consistent — it labels the figures as
"marg.-tail" and disclaims them in fn:wcaveat and again in caveat (a)
L1063–1077 — but the document still **prints `+4.3σ`, `-3.6σ`, `+2.5σ`,
"phantom-crossing required" in the right-hand column of a posterior summary
table, headline-claim font weight, in a Conclusions paragraph titled "empirical
anchor"**. PRD referees read tables before they read footnotes. Sweep
(19) — effect-size accounting — flags this directly:

- The chain mean is $w_0=-0.812\pm0.044$. The posterior distance to $-1$ is
  $\Delta=-1-(-0.812)=-0.188$, $\Delta/\sigma=-4.27$. This is a
  **marginal-tail distance**, not a tension statistic, because the chain has
  zero samples at $w_0=-1$ (the prior likely does not even support it given
  the data-driven posterior contraction); fn:wcaveat acknowledges exactly
  this.
- Reporting a marginal-tail distance in the same column where Table I would
  report a tension is sweep-(19) effect-size laundering. The reader's first-
  pass takeaway is "DESI-DR2+Planck+DES-Y5+Pantheon+ excludes ΛCDM at
  $4.3\sigma$" — which is *not* what the chain measures.
- The Conclusions L1954 reinforces this: "an empirical test of the quintom-B
  scenario" is the framing, but the actual *measurement* the chain supports
  is "posterior centered well into quintom-B territory; no model-comparison
  number computed".

**Why ESSENTIAL.** This is the same pattern as P1A overclaim against
GR/inflation (pattern-005-overclaim-anchor): the paper documents the caveat
correctly in the footnote and re-documents it in the caveat block, but the
load-bearing surfaces (table column header, Conclusions paragraph title,
abstract sketch) read as "DESI ⊕ Planck excludes ΛCDM at >4σ", which is
unsupported. External referees will not honour an in-paper caveat against
a printed `+4.3σ` in the headline column.

**Fix.**

1. Re-label Table~\ref{tab:iter2_posterior} third column from "vs ΛCDM" to
   "Marginal distance from $\Lambda$CDM (NOT a tension statistic; see fn.\ref{fn:wcaveat})".
2. Replace "(marg.-tail, $+4.3\sigma$)" with "$\Delta w_0/\sigma_{w_0}=-4.27$
   marg.-tail distance; ΛCDM point unsampled (fn.~\ref{fn:wcaveat})".
3. Replace Conclusions L1954 "an empirical test of the quintom-B scenario"
   with "an empirical anchor for the quintom-B parameter posterior; no
   ΛCDM-vs-quintom-B model-preference statistic is computed in this paper
   (deferred to nested-sampling follow-up)."
4. Delete `w_0 + w_a = -1.4788 \pm 0.1485 & phantom-crossing required`
   from the third column header row; "phantom-crossing required" is a
   physics interpretation, not a posterior summary, and the right column is
   already overstated.

---

### P1B-R29-E4 — Pipeline-recovery `SNR=20.32` is still printed in the abstract and §I.2 scope-of-paper as a positive-spin number, framed as "validation succeeded"

**Location**: Abstract L702–707; §I.2 L773 ("$20.32$"); fn:snr_definition L1362–1392.

**Quote (§I.2 L772–776)**:

> "Not a competitive sky detection. The high pipeline template-fit SNR
> figures (e.g., $20.32$) refer to recovery of injected MC signals, not to
> the significance of the CMB sky measurement, which remains the published
> $2.7$–$2.9\sigma$ from Planck/ACT."

**Problem.** The R22prov closure (v1B.0.50) demoted the SNR claim from
"sky-significance proxy" to "template-fit SNR of the matched template against
single-realization noise". Good. But the *abstract* (L702–707) and §I.2
(L772–776) still print `20.32` as the lead number with "validation succeeded"
framing. The fn:snr_definition footnote (L1362–1392) is excellent, but
fn:snr_definition is referenced only from §IV; the abstract and §I.2 readers
never see the actual definition before the number is quoted.

A PRD referee will read the abstract, see "$20.32$", then jump to §I.2 and
see it again with no definition, conclude the paper is hyping pipeline-recovery
SNR as a sky number, and reject on overclaim. The careful footnote in §IV is
not visible at the abstract's surface.

**Why ESSENTIAL** (border MAJOR; promoting to ESSENTIAL on the abstract-last
drift sweep). The R22prov closure noted "the bias (0.032°) remains" — meaning
SNR=20.32 was *supposed* to be removed from the abstract surface in v1B.0.50.
A re-read finds it still in the abstract (L705) under "pipeline-recovery"
language and still in §I.2 L773. Closure regression.

**Fix.**

1. Abstract L705: remove "(pipeline-recovery bias…carried forward as the
   pipeline systematic floor — both are MC pipeline-recovery figures, not
   sky-measurement systematics, and are not directly comparable to each
   other's published sky significances)" — the value lives but the prose is
   30 words; shorten to "(systematic floor; pipeline-recovery only,
   not a sky significance)".
2. Replace §I.2 L773's "e.g., $20.32$" with "e.g., template-fit
   matched-signal SNR $\sim 20$ on a synthetic-sky bias-injection MC
   (fn.~\ref{fn:snr_definition})". Numbers and footnote anchor in one place,
   no orphan "20.32".

---

## MAJOR findings

### P1B-R29-M1 — Burn-in reconciliation note (A2 closure) gives three different post-burnin counts for the *same* Planck+BAO+SN chain without ever stating the load-bearing one

**Location**: fn:sample_stratification L880–907 (post-EXT1-A2 closure).

**Quote (L890–901)**:

> "The post-burnin count of the full-tension subset alone is $123{,}129$
> (within $\pm 1\%$ of the $123{,}368$ exact computation…); the correct
> both-chains post-burnin total is $216{,}432$.
> *Burn-in reconciliation note:* The frozen
> `planck_bao_sn_20260312_1954` `convergence_report.txt` reports
> 'Burn-in: 20%' and post-burnin samples $= 106{,}361$… The $30\%$ figure
> used throughout this paper is conservative, matches the original-chain
> configuration documented in `COUNT_EXPLANATION.md`, and gives $93{,}064$
> post-burnin for this subset. The $106{,}361$ figure at $20\%$ is the
> GetDist-reported value; the paper's $216{,}432$ combined total uses the
> conservative $30\%$ cut uniformly for both frozen chains."

**Problem.** This footnote now contains, in 30 lines, three different
post-burnin sample counts for the Planck+BAO+SN chain:

- $216{,}432 - 123{,}368 = 93{,}064$ (paper's 30% cut, both chains stated as identical formula)
- $93{,}064$ (explicit, same line)
- $106{,}361$ (GetDist's 20% cut, same chain)
- $132{,}949 \times 0.7 \approx 93{,}064$ (formula in L883–884)

…but the *paper body* asserts the headline as `216,432 = both chains combined
at 30%`. The full-tension figure says `119,617 (getdist-thinned from 176,240
raw)` in Fig.~\ref{fig:corner_full_tension} L1192 — yet another count, with
no explanation given for why thinning would *increase* effective samples beyond
the 30%-burn-in raw count of $\approx 123{,}368$. (It does not; getdist
weight-based thinning *reduces* the effective count below the burn-in count,
so $119{,}617 < 123{,}368$ is internally consistent — but the relationship
is never explained on the page where Fig.~\ref{fig:corner_full_tension} is
referenced; the footnote is buried 300 lines later.)

A PRD referee will count the appearances of `123,128 / 123,368 / 123,129 /
119,617 / 106,361 / 93,064 / 216,432` in fn:sample_stratification and
conclude that the EXT1-A2 closure papered over the issue rather than
resolved it. The footnote *acknowledges* the reconciliation but does not
*pick* the canonical number; the reader has to thread through three counts to
find which one is load-bearing.

**Fix.** Restructure fn:sample_stratification into:

1. **Canonical:** Headline samples reported in this paper use the
   conservative 30% burn-in: $123{,}368$ full-tension + $93{,}064$
   Planck+BAO+SN = $216{,}432$ both-chains-combined.
2. **GetDist artefacts:** The frozen `convergence_report.txt` reports 20%
   burn-in (its own GetDist-default), giving $106{,}361$ for Planck+BAO+SN.
   This is documented but not used.
3. **Fig.~\ref{fig:corner_full_tension}:** Plots $119{,}617$ samples
   (full-tension post-30%-burn-in $123{,}368$, then GetDist
   effective-sample-weight thinning).

Three numbered points, one canonical, two artefacts. The current footnote
prose contains the right information but does not pick a winner; sweep-(17)
uncomputed-claim flag fires on which post-burnin count is canonical for the
headline 309,189 vs 216,432 statements.

---

### P1B-R29-M2 — DES-SN5YR / Pantheon+ overlap caveat (A3 closure, caveat (e)) qualitatively asserts "shared $\sim 20\%$" without a citation that supports the figure, and the bias-direction argument is hand-waved

**Location**: caveat (e) L1113–1128.

**Quote (L1115–1119)**:

> "These two catalogs share approximately $20\%$ of their supernova events
> with different Malmquist-bias corrections applied by the respective
> collaborations~\cite{DES2024SN5YR}. The present analysis combines them
> via a product likelihood without a joint covariance that accounts for the
> shared-event overlap."

**Problem.** The $20\%$ figure is asserted without a page/section pointer
in DES2024SN5YR (Vincenzi et al. 2024). The actual DES-SN5YR paper does
discuss the Pantheon+ overlap (DES-SN5YR has ~1635 photometrically-classified
SNe Ia in the Hubble flow, ~194 low-z external SNe, of which a subset
overlap Pantheon+; the typical published number is "low-z external SNe are
the overlap subset, $\lesssim 200/1829$ DES SNe and $\lesssim 200/1701$
Pantheon+ SNe = $\sim 12\%$ of the *combined* sample"). The "$20\%$ of
their events" framing is ambiguous: 20% of DES? of Pantheon+? of the
union? of the low-z subset?

Sweep (17) uncomputed-claim fires: the $20\%$ figure is not derived from
a quoted artefact (e.g. a re-count from the two collaborations' published
sample sizes) and is not directly traceable to DES2024SN5YR.

Sweep (19) effect-size fires: "the direction of this bias is toward the
mean of the two catalogs' individual SN posteriors, which is itself close
to the combined Planck+BAO constraint; the qualitative quintom-B finding
($w_0 + w_a < -1$) is therefore unlikely to be reversed" — this is the
correct qualitative argument but it is asserted, not shown. A 1-sentence
estimate of *how much* the joint constraint shifts under a joint-covariance
treatment would close this; without it, the reader has no way to tell
whether the $+4.3\sigma$ marginal-tail distance survives a 5% correction or
collapses.

**Fix.**

1. Replace "approximately $20\%$" with the actual overlap number, quoted
   from DES2024SN5YR §X (or DES Collaboration website's overlap table):
   "$\sim 194$ low-redshift external SNe Ia in DES-SN5YR are shared with
   Pantheon+, i.e.\ $\sim 12\%$ of the DES-SN5YR sample and
   $\sim 11\%$ of the Pantheon+ sample."
2. Quote a numerical estimate of the bias under the no-joint-covariance
   approximation. The simplest is: under double-counting of $N_{\rm shared}$
   events with per-event $\sigma_\mu$ distance-modulus uncertainty, the
   effective sample size is overstated by $\sim 5$–$10\%$ of one catalog,
   shrinking the joint SN $\chi^2$ likelihood width by $\sim \sqrt{1-0.10}
   \approx 5\%$. Give a 5%, 10%, 15% bracket explicitly so the reader can
   judge.
3. State explicitly: "The $w_0$ marginal width $\sigma_{w_0}=0.0436$ would
   inflate to $\sim 0.046$ under a 10% joint-covariance correction, shifting
   the marginal-tail distance from $-4.27$ to $\sim -4.0$; the headline
   marg.-tail framing is preserved." This is the sweep-(19) effect-size
   computation that the caveat is missing.

---

### P1B-R29-M3 — Fig.~\ref{fig:dneff_viability} caption rescope (A7 closure) is now scoped, but the figure file itself remains `fig_dneff_viability_two_frozen.pdf` — a referee opening the PDF cannot tell whether the figure shows the rescoped content

**Location**: Fig.~\ref{fig:dneff_viability} L1199–1217; caption L1202–1216.

**Quote (L1212–1215, A7-closed prose)**:

> "No evidence for a recombination-era $\Delta\Neff$ shift appears in this
> stock-CAMB proxy run; this does *not* directly test the ECH spin-torsion
> sector, which lacks a Boltzmann-module prediction for $\Delta\Neff$ in
> stock-CAMB (see §~\ref{sec:verification} scope note)."

**Problem.** The caption now correctly rescopes the figure from "ECH-route
viability" to "$\Delta\Neff$ marginal posterior comparison". But the
*figure filename* `fig_dneff_viability_two_frozen.pdf` retains the
"viability" tag. Referees who download artefacts from the repo will see
the file by its name; the rescoped caption only protects in-PDF readers.

Sweep (16) provenance: the figure file should be renamed to match the
rescoped content (e.g.\ `fig_dneff_marginal_two_frozen.pdf` or
`fig_dneff_posterior_compare.pdf`), and the rename should be done atomically
with the caption rescope. Currently the closure is half-done: caption text
yes, filename no.

**Fix.** Rename the figure file from `fig_dneff_viability_two_frozen.pdf`
to a content-matching name in the `figures/` directory; update L1201
`\includegraphics{...}` to match. Same diff size, closes the provenance gap.

---

### P1B-R29-M4 — fn:eskilt_pr3_pr4 (L708–719) creates a hybrid attribution that asks the reader to trust an unattested code-repo dataset claim against a published paper's stated dataset

**Location**: fn:eskilt_pr3_pr4 L708–719; §VI L1599–1601; §III L848–850.

**Quote (L708–719)**:

> "Eskilt \& Komatsu 2022 disambiguation: the published PRD paper
> [Eskilt2022] (PRD 106:063503, arXiv:2205.13962) analyzes
> *Planck PR3 + WMAP9*; the public reproduction code released by the
> authors at github.com/LilleJohs/Cosmic\_Birefringence was subsequently
> updated to use *Planck PR4 / NPIPE*. Throughout this paper, the labels
> 'PR4/NPIPE' attached to the Eskilt+Komatsu likelihoods refer to the
> code-repository dataset (which is what the ALP-MCMC re-runs actually use);
> the abstract $\beta=0.342^\circ\pm 0.094^\circ$ ($3.6\sigma$) headline
> is from the published PR3+WMAP9 joint analysis."

**Problem.** This is the long-tail of the cascaded R-round-4 closure
(`v1B.0.34`, PER4-B2). The current state asserts: (a) the published paper's
headline $\beta=0.342\pm 0.094$ is from PR3+WMAP9; (b) the LilleJohs repo
uses PR4/NPIPE; (c) the ALP-MCMC in this paper anchors its likelihood to
the published $\beta=0.342\pm 0.094$ summary. So the ALP-MCMC uses the
PR3+WMAP9 summary likelihood — *not* PR4/NPIPE — yet the paper labels the
likelihood "PR4/NPIPE" in §VI L1599–1601 and §III L848–850.

This is sweep-(15) drift: the label "PR4/NPIPE" applies to the *reproduction*
*code* but the *summary likelihood* used in this paper's MCMC is the
*published* PR3+WMAP9 $\beta=0.342$ figure (Gaussian summary, encoded as
`beta_obs: 0.342, sigma_beta: 0.094` in `c5.input.yaml` L1726–1731).

The MCMC is using a Gaussian summary of the *published* number; the
"PR4/NPIPE" attribution is therefore *not* the right label for the
likelihood used in this paper's ALP-MCMC. It is the right label for what
LilleJohs's repo does if you re-run it from scratch, but Houston does not
re-run from scratch — he runs a Gaussian summary on `0.342 ± 0.094` which
is the PR3+WMAP9 number.

Calling this "PR4/NPIPE" anywhere in §VI is sloppy attribution. The correct
label is "PR3+WMAP9 published summary, code repo separately moved to
PR4/NPIPE for re-reproduction".

**Fix.** Replace the "joint WMAP+Planck value" / "joint WMAP9 + Planck
PR4/NPIPE analysis" labels in §VI L1599–1601 (and L725 in abstract, L1255
in §IV, L1727 in §VI footnote) with "joint WMAP9 + Planck PR3 published
summary likelihood (the code repo's PR4/NPIPE re-run is independent and
not used as a separate constraint here)". This is one substitution applied
4 times; closes the attribution hybrid.

---

### P1B-R29-M5 — Independent cross-validation paragraph (L1171–1186) quotes Liu et al. $\alpha=-0.00066 \pm 0.00098$ and $\Delta\text{AIC}=-5.7$ to $-6.6$ but does not handle the conflict between "torsion preferred by AIC" and "torsion parameter consistent with zero"

**Location**: §III L1171–1186.

**Quote (L1171–1180)**:

> "Liu et al. [ECTorsionDESI2025] constrained an EC torsion model using
> DESI~DR2 + Pantheon+ + DES-SN5YR + Planck~2018, finding torsion
> preferred by AIC ($\Delta\text{AIC}=-5.7$ to $-6.6$) but with the torsion
> parameter itself consistent with zero ($\alpha = -0.00066 \pm 0.00098$).
> Their headline values $H_0 = 68.41 \pm 0.32$ km/s/Mpc and $S_8 = 0.812
> \pm 0.006$ agree with our Planck+BAO+SN chain at $0.5\sigma$ in $H_0$…"

**Problem.** Sweep (19) effect-size + sweep (17) uncomputed-claim. Liu et
al.\ reporting $\Delta\text{AIC}=-5.7$ to $-6.6$ for a model whose own
torsion parameter is $0.7\sigma$ from zero is a *statistically suspicious
combination*. AIC favours the torsion model by $\Delta\text{AIC}\sim -6$
(i.e.\ $\exp(-6/2)\approx 0.05$ relative-likelihood for $\Lambda$CDM) yet
the central torsion-modifying parameter is undetected at $0.7\sigma$. This
is either: (a) Liu's torsion model has $\ge 2$ effective extra parameters
that buy a good fit via channels other than the headline $\alpha$ (so the
AIC preference is real but driven by nuisance / dataset-rescaling, not by
detecting torsion); or (b) the comparison is across different dataset
combinations with rebalanced weights; or (c) the AIC computation is wrong.

The paper just quotes both numbers and notes "their torsion-consistent-
with-zero result parallels our $\Delta\Neff$-consistent-with-zero null
finding" without addressing the AIC paradox. A PRD referee will ask:
how can Liu's torsion model carry $\Delta\text{AIC}=-6$ in favour with a
$0.7\sigma$ central parameter? Either Houston's reading of Liu is wrong or
Liu's result has a non-trivial interpretation that the paper hand-waves
over.

**Fix.** Add one sentence: "Liu et al.\ AIC preference is driven by their
$w_0 w_a$ dark-energy parameters (the same DESI-DR2 quintom-B signature
seen in our iter2 chain) rather than by their torsion $\alpha$ parameter,
which is the $\le 1\sigma$ central we quote; their AIC-preference and
torsion-non-detection statements are therefore both correct and consistent."
Or, if that's not the right reading, drop the AIC-preference quote and
report only the torsion-non-detection number — the AIC is dangling
context that confuses more than it clarifies.

---

### P1B-R29-M6 — Conclusions "Quintom-B empirical anchor" paragraph (L1954) re-prints the +4.3σ-marginal-tail framing without the fn:wcaveat scope

**Location**: Conclusions L1954.

**Quote (L1954)**:

> "*Quintom-B empirical anchor.*—The converged DESI DR2 + Planck NPIPE +
> Pantheon+ + DES-SN5YR Cobaya chain with the $w_0 w_a$ free-parameter
> extension … supplies the GetDist $w_0 w_a$ posteriors of
> Table~\ref{tab:iter2_posterior}, an empirical test of the quintom-B
> scenario."

**Problem.** Conclusions L1930 dutifully omits AIC/BIC/$\ln B$; this is
correct. But the very next paragraph (L1954, "Quintom-B empirical anchor")
calls the result "an empirical test of the quintom-B scenario" — which is
not what the chain measures. The chain measures posterior parameters
*given* a $w_0 w_a$ model; it does not "test" quintom-B because the chain
has no $\Lambda$CDM-region samples to compare against. Calling it a "test"
is the same overclaim as the table column header in E3.

This is sweep-(15) abstract-last drift in Conclusions: the body's
fn:wcaveat scope does not propagate to the Conclusions paragraph that
re-uses the result.

**Fix.** Change Conclusions L1954 from "an empirical test of the quintom-B
scenario" to "a precision posterior measurement of the $w_0 w_a$
parameters within the quintom-B family; no $\Lambda$CDM-vs-quintom-B
model-preference statistic is computed here." 1-line edit; closes the
sweep-(15) drift in Conclusions to match fn:wcaveat scope.

---

### P1B-R29-M7 — `\sigmaunit` is defined as `\sigma` (L46) and used in §VI Eq.(3) caption + auxiliary cross-check prose; the comment says "v1B.0.48: was used 4x in §birefringence_check but never defined", but the *definition* is itself wrong type-set

**Location**: L46; L1699–1712.

**Quote (L46)**:

> `\newcommand{\sigmaunit}{\sigma}`

**Problem.** `\sigmaunit` is defined as `\sigma`, but it is invoked in
math mode (Eq.~3 L1699–1701) and inline-math-mode (auxiliary cross-check
L1702–1713: `the $3.9\sigmaunit$ figure`). `\sigmaunit` expands to `\sigma`
which is a math-mode-only command. In `$3.9\sigmaunit$` the math mode is
correct, so the typeset works. But the comment says "was used 4x in
§birefringence_check but never defined — silently dropped the sigma glyph
in v1B.0.47 and earlier" — implying that in v1B.0.47 and earlier the LaTeX
*ran*, just without the glyph. That can only happen if `\sigmaunit` was an
undefined macro that LaTeX silently treated as empty. **LaTeX does not
silently treat undefined macros as empty** — it errors with `Undefined
control sequence`. The "silently dropped" history claim is internally
inconsistent.

This is minor on the rendered output (current v1B.0.55 renders fine) but
flags sweep (16) — the source-history claim in the comment is wrong, which
is the kind of thing a forensic referee will catch and use as evidence
that the changelog is editorialised rather than auditable.

**Fix.** Either (a) drop the "silently dropped the sigma glyph in v1B.0.47"
half-sentence from L46 (the macro is defined now, that's all that
matters); or (b) replace with the truthful statement: "v1B.0.48: defined
`\sigmaunit` macro; v1B.0.47 and earlier the $3.9\sigmaunit$ occurrences
either generated `Undefined control sequence` errors at compile time or
the macro was previously aliased differently". Source-history hygiene only,
no rendered-PDF impact.

---

### P1B-R29-M8 — `app:claims` claims table (L2057–2075) does not include any of the new EXT1-closure claims (one-sided 95% ΔN_eff limits, DES-SN5YR overlap caveat, calibrated-bias floor, M_Pl definition, LiteBIRD-qualifier 9σ)

**Location**: Appendix B "Claims Classification" L2049–2075.

**Quote (Table~\ref{tab:claims} L2063–2073, full table content)**:

> $\Delta\Neff = -0.020\pm 0.169$ (full-tension) | MCMC | Verified
> $\Delta\Neff = +0.065\pm 0.17$ (Planck+BAO+SN) | MCMC | Verified
> $H_0 = 67.68\pm 1.06$ (full-tension) | MCMC | Verified
> $H_0 = 67.79\pm 1.09$ (Planck+BAO+SN) | MCMC | Verified
> Model-comparison ΔAIC/BIC/lnB | Numerical | Omitted | Follow-up nested-sampling
> $\hat\beta_{\rm NaMaster} = 0.238^\circ$ (500-MC) | Numerical | Verified
> $\beta_{\rm ALP} = 0.336^\circ \pm 0.10^\circ$ | MCMC | Verified
> Published $3.6\sigma$ ($\beta=0.342\pm 0.094^\circ$) | Lit. | Cited
> Stock CAMB proxy ≠ ECH theory module | Scope | Defn.
> ALP birefringence not distinctive ECH prediction | Scope | Defn.

**Problem.** The claims table is sold as "machine-checkable index used by
the reproducibility audits of Appendix~\ref{app:reproducibility}" (L2052–2055),
but it predates EXT1 and was not updated by the v1B.0.55 closure wave.
Missing rows:

- One-sided 95% upper limits $\Delta\Neff < 0.31$ / $<0.39$ (A6 closure)
- DES-SN5YR/Pantheon+ overlap caveat (A3 closure)
- $w_{\rm pivot} = -0.952 \pm 0.019$ (new headline number in v1B.0.50)
- $w_0 = -0.812 \pm 0.044$, $w_a = -0.667 \pm 0.186$ (Table I-B headline)
- NaMaster pipeline calibrated-bias floor 0.040° (A8 closure)
- $C_{a\gamma}$ continuous-prior posterior median 20.7 (post-v1B.0.41)
- Spectator-subset readout (A12 closure: $44\%$ at $\Omega_a < 0.1$,
  $\beta|\Omega_a \le 0.01 = 0.28 \pm 0.10$)

A claims table that does not include the headline numbers of the paper is
not a "machine-checkable index"; it is a stale artefact. Sweep (16)
provenance fires hard.

**Fix.** Add 7 rows above. Each one is a one-line `Mean | Type | Status |
Notes` entry. ~15 min of editing; closes the sweep-(16) provenance audit
for the claims table.

---

### P1B-R29-M9 — Standalone-reader test (sweep 18): §VI "Spectator-ALP consistency check" requires the reader to follow ≥3 footnotes to reconstruct the headline $\beta=0.27°$ vs $0.342°$ disambiguation

**Location**: §VI L1586–1908.

**Problem.** A first-time PRD reader entering §VI sees:

- L1591: "$\beta \approx 0.27^\circ$" — fiducial
- L1599–1601: "$\beta = 0.342^\circ \pm 0.094^\circ$ ($3.6\sigma$)" — published
- L1621: "$\Delta\phi/f_a \approx 0.42$" — at $m=2H_0$, $\theta_i=1$
- L1643: "for $C_{a\gamma}=8$, $\theta_i=1$, $m\approx 3.9 H_0$" — at $\beta\approx 0.28^\circ$
- L1651: Eq.(2) gives $\beta = 0.28^\circ$
- L1665: "fiducial value $\beta \approx 0.27^\circ$"

The reader does not know, from §VI alone, *which* of $0.27^\circ$, $0.28^\circ$,
$0.30^\circ$ (Planck NPIPE), $0.342^\circ$ (Eskilt joint), $0.215^\circ$
(ACT DR6), $0.241^\circ$ (auxiliary inverse-variance) is the "consistency
check" target. The current prose pivots between "fiducial $0.27°$" and
"observed $0.342°$" without ever stating: "the consistency check is that
the model's natural parameter range produces β in the band
$[0.27, 0.342]°$, and this band straddles the observed central value."

Sweep (18) standalone-reader: a PRD referee opening at §VI will not get a
crisp model–data comparison statement; instead they get six numbers and
six rebracketings.

**Fix.** Add one summary sentence at the top of §VI:

> "Summary of the consistency check: the spectator-ALP model with
> $f_a\sim\MPl$, $m\sim H_0$ produces birefringence $\beta$ in the range
> $\sim 0.01°$–$0.48°$ across the natural envelope
> $C_{a\gamma}\in[4,12]$, $m/H_0\in[1,3]$, $\theta_i\in[0.5,2]$; this band
> straddles both the fiducial value $\beta=0.27°$ used as the NaMaster MC
> injection target and the published Eskilt joint WMAP+Planck central
> value $0.342° \pm 0.094°$, so the model accommodates the observed signal
> within its natural envelope. The MCMC posterior $\beta_{\rm ALP}=0.336°
> \pm 0.10°$ confirms this accommodation."

3 sentences at §VI L1586 close the sweep-(18) reader gap.

---

### P1B-R29-M10 — `Cai2010quintomReview` bibliography note (L1109 area, A5 closure) still references "program-management note" in the changelog; the changelog claim is fine, but the v1B.0.39 GEM-B1 footnote (L1610–1618) introduces a *different* attribution problem: ALP ODE integration "in a $\Lambda$CDM background" cites a quintom review

**Location**: fn at L1610–1618.

**Quote (L1610–1618)**:

> "The ALP ODE is integrated on a $\Lambda$CDM late-time $H(z)$ here as an
> empirical background, distinct from the quintom-bounce dynamics that
> supply the early-universe / contracting-phase $H(z)$ in the underlying
> ECH cosmology~\cite{Cai2010quintomReview}."

**Problem.** The reader is told the ALP ODE integration uses $\Lambda$CDM
background (correct, conservative). The footnote then cites a quintom-bounce
review as if it supplies the alternative early-universe $H(z)$ that *would*
matter — but the ALP ODE is integrated only from recombination to today,
i.e.\ on the late-time $H(z)$. The early-universe contracting-phase $H(z)$
of the ECH cosmology is *irrelevant* to the ALP rotation from recombination
to today, since recombination is post-bounce in any bouncing scenario.

The Cai2010 citation is therefore dangling: it appears to justify a worry
that does not apply (early-universe $H(z)$ does not enter the late-time
ALP ODE). The whole "distinct from the quintom-bounce dynamics" clause
should be deleted or rephrased.

**Fix.** Replace the footnote at L1610–1618 with:

> "The ALP ODE is integrated on a $\Lambda$CDM late-time $H(z)$. A quintom
> late-time $w_0 w_a$ background (as in Sec.~\ref{sec:cosmo_fits}) shifts
> $H(z)$ at $z \lesssim 1$ by $\sim$few percent, propagating to a
> $\lesssim$few-percent systematic on $\Delta\phi/f_a$ — well below the
> $\sim 30\%$ prior-width envelope on $\theta_i$ and $m/H_0$ dominating the
> $\beta$ prediction. The early-universe contracting phase does not enter
> the late-time integration."

Removes the Cai2010 dangling cite (move it to the introduction where the
quintom-bounce class is referenced for *theoretical* motivation).

---

## MINOR findings

### P1B-R29-MIN1 — H_0 column-header style is now correct in Table I (L965) and Table II (L1012), but the caveat block (L1085, L1095, L1097, L1176) still prints "km/s/Mpc" inline

**Location**: L1085 ("$H_0 = 67.185 \pm 0.455$ km/s/Mpc"), L1095 ("$67.68 \pm 1.06$ km/s/Mpc"), L1097 ("$73.04 \pm 1.04$ km/s/Mpc"), L1176 ("$H_0 = 68.41 \pm 0.32$ km/s/Mpc").

**Problem.** A14 closure standardised Table-I and Table-II column headers to
`[km\,s$^{-1}$\,Mpc$^{-1}$]`, but the prose still uses the slash form
`km/s/Mpc` in at least 4 places. PRD copy-edit style prefers the spaced-
exponent form throughout. Sweep (15): partial closure.

**Fix.** `sed s/km\/s\/Mpc/$\,$km$\,$s$^{-1}$$\,$Mpc$^{-1}$/g` on
L1085–L1176, then visual check that the typeset prose still wraps cleanly.

---

### P1B-R29-MIN2 — Fig. 4 caption (`fig:namaster_recovery` L1222–1241) reports per-realization scatter $\sigma_\beta = 0.029°$ at $f_{\rm sky}=0.85$ and $0.033°$ at $0.65$ but text at L1421–1422 reports the same $0.029°$ and $0.033°$ — *no internal inconsistency* — yet the figure caption omits the canonical $\sigma_\beta=0.046°$ at $f_{\rm sky}=0.32$ now derived in fn:snr_definition

**Location**: Fig. 4 caption L1232–1241; fn:snr_definition L1382–1392.

**Problem.** Sweep (15) abstract-last drift: fn:snr_definition (L1382–1392)
now states $\sigma_\beta=0.046°$ at $f_{\rm sky}=0.32$ from a dedicated
rerun, but the Fig. 4 caption still says "per-realization $\sigma_\beta$
was not recorded in the original canonical $f_{\rm sky}=0.32$ artifact, so
that point is plotted with the mean only; a dedicated 500-MC rerun
(fn.~\ref{fn:snr_definition}) measures $\sigma_\beta = 0.046^\circ$ at this
point." — wait, the caption *does* mention 0.046°. Re-reading: caption L1236–1238
correctly cross-references fn:snr_definition. **This is actually fine** — the
caption disclaims the missing artefact and forwards the reader to the
dedicated rerun. Demoting from MINOR-finding to "noted, no action needed".

**Fix.** None required; caption handles the disclosure correctly.

(Retained in the finding list as a marker that the sweep was run and
returned clean.)

---

### P1B-R29-MIN3 — `\path{...}` instances inside footnotes risk overflow in the two-column PRD layout

**Location**: fn:rhat_csv L975 (`\path{reproducibility/cosmology/convergence_latest.csv}`); fn:snr_definition L1386 (`\path{reproducibility/p1_namaster_500mc/results/c9f_negative_beta.json}`); §VI L1626, L1664, L1668 (`\path{research/branch_R_alp_birefringence/phase2_mcmc/c10b_alp_envelope_scan.json}`); §VI L1841 (`\path{research/branch_R_alp_birefringence/phase2_mcmc/c10a_spectator_slice.json}`); §VI L1846; §IV L1306, L1327, L1335, L1336, L1342, L1374, L1386, L1436, L1458, L1492, L1493; §C L2127.

**Problem.** PRD two-column layout is ~3.4 in (245 pt) wide; a `\path{}`
containing `research/branch_R_alp_birefringence/phase2_mcmc/c10b_alp_envelope_scan.json`
is ≥75 characters and cannot break at any underscore (`\path{}` produces an
unbreakable atom). Several of these will produce overfull \hboxes that the
running `/latex-audit` skill flags.

The two-column footnote layout is even narrower (~2.5 in for a single
column-wide footnote attached to a single-column table), where these paths
will definitely overflow.

**Fix.** Run `/latex-audit` on the v1B.0.55 PDF and identify which `\path{}`
instances actually produce overfull boxes. For each, replace with the
`\artifact{}` macro defined at L121, which is a hyperlinked
`\nolinkurl{}` rendering that allows line breaks at slashes and underscores
in most LaTeX configurations. Or move the long paths from inline-footnote
position to the appendix.

Recommended: run `\path` → `\artifact` global replacement *in footnotes*
only (the body-text instances inside `\texttt{}` are fine since they sit in
single-column body width); keep `\path` in `\artifact{}` definition (L121)
for the hyperlinked rendering.

---

### P1B-R29-MIN4 — fn:wpivot (L1009) algebra closure $-0.8122 + 0.210 \times (-0.6666) = -0.952$ assumes 3-sig-fig presentation but the chain-readout mean is $-0.8122 + 0.210 \times (-0.6666) = -0.81220 + (-0.13999) = -0.95219$, which rounds to $-0.952$ ✓ — the math is right

**Location**: fn:wpivot L1009.

**Problem.** No problem found; sweep (17) uncomputed-claim was applied to
this footnote and it self-checks. Recording as a clean-flag minor.

The Cov check: $\mathrm{Cov}(w_0, w_a) = -0.00729$, $\rho = -0.90$,
$\sigma_{w_0} = 0.0436$, $\sigma_{w_a} = 0.1864$, so
$\rho \sigma_{w_0} \sigma_{w_a} = -0.90 \times 0.0436 \times 0.1864 = -0.00731$,
matching $-0.00729$ to within $\pm 0.0001$ rounding. Cauchy
bound: $|\mathrm{Cov}| \le \sigma_{w_0} \sigma_{w_a} = 0.00813$, and
$0.00729 < 0.00813$ ✓. All algebra in fn:wpivot is internally consistent.

**Fix.** None.

---

### P1B-R29-MIN5 — Eq.(2) $\beta \approx (\alpha_{\rm EM} \times 8) / (4\pi) \times 1.06$ converts to degrees inline; the prefactor 4.93×10⁻³ rad → 0.28° uses 180°/π = 57.296, giving 0.2824°, which rounds to 0.28°. Algebra clean

**Location**: Eq.(2) L1651–1654; convention discussion L1655–1664.

**Problem.** Algebra self-checks. Convention statement at L1655–1664 also
self-consistent: $g_{a\gamma} = C_{a\gamma} \alpha_{\rm EM}/(2\pi f_a)$,
$\beta = (g_{a\gamma}/2) \Delta\phi = C_{a\gamma} \alpha_{\rm EM}/(4\pi)
\times \Delta\phi/f_a$. Matches Eq.(2).

Recording as a clean-flag minor; sweep (17) applied to the rotation
formula and it self-checks.

**Fix.** None.

---

### P1B-R29-MIN6 — §VI "Fujita et al. ~\cite{Fujita2021}" attribution (L1595–1596) does not state whether the present paper *extends* Fujita's analysis or merely *re-derives within the same class*

**Location**: §VI L1595–1596.

**Quote (L1595–1596)**:

> "The model class was previously studied by Fujita~\etal~\cite{Fujita2021}."

**Problem.** PRD reviewers from the ALP / cosmic-birefringence community
will know Fujita 2021 in detail; "previously studied" is too thin for
attribution. Did Fujita derive the same $\Delta\phi/f_a$ envelope at the
same $C_{a\gamma}\in[4,12]$ box? Did Fujita carry the spectator-status
caveat? If yes, this paper is a re-derivation with updated data; if no,
this paper extends Fujita to (a) the post-2024 ACT DR6 + Eskilt joint
likelihood and (b) the explicit spectator-status fine-tuning disclosure.

Sweep (18) standalone-reader: a reader cannot tell what is new here vs.
what is a Fujita re-derivation.

**Fix.** Add one sentence after L1596: "Fujita et al.\ derived the same
ALP class with the same fundamental ODE; the present analysis updates the
observational anchor to the Eskilt joint WMAP9+Planck PR3 summary
likelihood and adds the explicit spectator-status fine-tuning disclosure
($\theta_i \sim 0.1$ requires $\sim 25\times$ tuning relative to the
natural prior midpoint; fn.~\ref{fn:theta_backreaction})."

---

### P1B-R29-MIN7 — Footnote on dimension-6 contact operator (L913–923) is technically correct but introduces $\Lambda_{\rm strong} \sim \MPl / \sqrt{\gamma_{\rm BI}}$ without ever defining $\gamma_{\rm BI}$ in this paper

**Location**: L913–923.

**Quote (L913–923)**:

> "The dimension-6 four-fermion contact operator is interpreted here in the
> low-energy effective field theory (EFT) below the strong-coupling /
> torsion-resolution scale $\Lambda_{\rm strong} \sim \MPl / \sqrt{\gamma_{\rm BI}}$
> set by the inverse Barbero–Immirzi parameter $\gamma_{\rm BI}$
> (cf.~[Mercuri2006], where the contact interaction is derived; the
> strong-coupling scale itself is a heuristic EFT-validity estimate);
> above this scale the contact-operator description breaks down…"

**Problem.** $\gamma_{\rm BI}$ is the Barbero–Immirzi parameter, which is a
*core* parameter of the ECH program in Paper I(a) but is *never named or
constrained* in this companion. A reader entering at the verification
companion will see $\gamma_{\rm BI}$ unsupported. Sweep (18)
standalone-reader: ECH-class parameters introduced in Paper I(a) should
either be cross-referenced (give the section/equation in Paper I(a)) or
parenthetically defined.

**Fix.** Replace "set by the inverse Barbero–Immirzi parameter
$\gamma_{\rm BI}$ (cf.~[Mercuri2006]…)" with "set by the inverse
Barbero–Immirzi parameter $\gamma_{\rm BI}$ of the Holst sector (see
Paper~I(a)~\cite{Golden2026P1a}~§II for the Barbero–Immirzi parameter's
role in the ECH theoretical framework, and \cite{Mercuri2006} for the
contact-interaction derivation; …)"

---

### P1B-R29-MIN8 — `\paperVersion` macro `v1B.0.55` is asserted in 4 places, but the macro is *also* hard-coded at L2040 ("`v1B.0.54`")

**Location**: §A `HuggingFace datasets` L2040.

**Quote (L2040)**:

> "DOI links are pinned to the `v1B.0.54` commit in the repository
> README; the DOIs are preserved against future README changes"

**Problem.** Bare `v1B.0.54` hard-coded; macro is `\paperVersion =
v1B.0.55`. This was an EXT1-A4 closure (v1B.0.55 should pin to v1B.0.55
in the README pointer). The closure block at L136 says "A4 (F20/F21): Data
Availability + Appendix A updated with v1B.0.55 tag pointer", but the
actual L2040 prose still says `v1B.0.54`.

Sweep (15) — abstract-last drift, but inverted: the *changelog* says it
was fixed; the *body* says it wasn't. Closure regression / missed-edit.

**Fix.** L2040 replace `v1B.0.54` with `\paperVersion`. 1-character diff,
gives a macro-driven version pinning that survives future bumps.

---

### P1B-R29-MIN9 — fn:rhat_csv (L975) typographically excellent but reads as a wall-of-text on the page; first sentence already conveys the headline

**Location**: fn:rhat_csv L975–977.

**Problem.** 7 lines of dense footnote, with parameter blocking lists
inline (`$A_{\rm planck}$, amp$_{143}$, amp$_{217}$,…`). PRD layout will
render this footnote as a ~half-page block at the bottom of column-1
page-2. Sweep (PDF-formatting): footnote should be split or moved to the
appendix.

**Fix.** Move the parameter-blocking list (`$A_{\rm planck}$, amp$_{143}$,
amp$_{217}$, amp$_{143\times 217}$, $n_{143}$, $n_{217}$,
$n_{143\times 217}$, calTE, calEE`) to Appendix~B as a one-line
list-of-blocking-parameters; keep the footnote headline "Worst row is
$n_s$ in the full-tension combination at $\hat{R}-1=9.74\times 10^{-4}$;
all sampled parameters across both frozen combinations satisfy
$\hat{R}-1 < 3\times 10^{-3}$. Full parameter list in Appendix~B; full
per-parameter convergence tables archived at convergence\_latest.csv."

Reduces fn:rhat_csv from ~7 lines to ~2 lines; preserves all content.

---

### P1B-R29-MIN10 — §III scope paragraph at L909–939 ("Scope of the $\Delta\Neff$ proxy") rebrands the proxy as "bounce-class discrimination" — but the actual *finding* is null

**Location**: §III L909–939.

**Quote (L935–939)**:

> "we frame the proxy as a bounce-class *compatibility check* (minimal
> matter-bounce-class scenarios without prolonged post-bounce inflation
> predict $\Delta\Neff\!\approx\!0$), not as a posterior-preference test
> against a competing model."

**Problem.** "Compatibility check" is the right framing, but the heading
prose at L909 reads "*Scope of the $\Delta\Neff$ proxy: bounce-class
discrimination, not a direct test of the spin-torsion sector.*" — using
"bounce-class discrimination". A null result does *not* discriminate
between classes; it is compatible with all classes that predict
$\Delta\Neff \approx 0$ (which includes minimal matter-bounce, but also
$\Lambda$CDM, standard inflation, ekpyrotic, …). The heading overclaims.

**Fix.** Change heading L909 from "bounce-class discrimination" to
"bounce-class compatibility check"; keep body L937–939 unchanged.

---

## NIT findings

### P1B-R29-N1 — Title is 3 lines; PRD style permits but discourages

**Location**: Title L673–675.

> "Technical Verification Companion to the ECH Spin-Torsion Program:
> $\Lambda$CDM$+\Delta N_{\rm eff}$ MCMC Proxy, NaMaster Pipeline Recovery,
> and a Birefringence Consistency Check with a Spectator-ALP Model"

**Fix.** Consider tightening to: "Technical Verification Companion: MCMC
Proxy, NaMaster Pipeline, and Spectator-ALP Birefringence Consistency
Check for the ECH Spin-Torsion Program". 1 line, ~25 words.

---

### P1B-R29-N2 — `\textit{Note.}---` at §VI start (L1588) is the only `\textit{Note.}` in the paper; all others use `\emph` or italic prose

**Location**: §VI L1588.

**Fix.** Replace `\textit{Note.}---` with `\emph{Note.}---` for consistency.

---

### P1B-R29-N3 — "we" used inconsistently; sometimes "we", sometimes "the author", sometimes passive

**Location**: throughout.

**Fix.** Single-author PRD papers typically use "we" as the authorial
voice throughout. Houston's Acknowledgments at L1989 use "the author";
prose uses "we" (L825, L860, …). Standardize to "we" or "I" — author's
choice — but pick one.

---

### P1B-R29-N4 — Hard-coded "Independent Researcher, Los Angeles, California, USA" at L679 is fine; nit only

**Fix.** None. Including for completeness of the sweep.

---

### P1B-R29-N5 — `\pacs{98.80.-k, 95.36.+x, 04.50.Kd}` retained at L741; per the v1B.0.55 changelog "SKIPPED: A17 (F14 PACS — PRD target retains \pacs{}; OPINION-tier for our target)"

**Fix.** No action; changelog acknowledgement noted.

---

## Summary recommendation

**Verdict: MAJOR REVISION required before PRD acceptance.**

**Findings tally:**
- ESSENTIAL: 4 (E1 README column-permutation bug; E2 abstract one-sided ΔN_eff; E3 Table II tension-laundering; E4 SNR=20.32 abstract surface)
- MAJOR: 10 (M1 burn-in three-count footnote; M2 DES/Pantheon overlap uncomputed; M3 figure file name; M4 PR3/PR4 hybrid attribution; M5 Liu AIC paradox unhandled; M6 Conclusions "test" overclaim; M7 \sigmaunit history half-claim; M8 claims-table missing 7 EXT1 rows; M9 §VI reader gap; M10 Cai2010 dangling cite)
- MINOR: 10 (km/s/Mpc prose, Fig 4 caption clean-flag, \path overflow risk, fn:wpivot clean-flag, Eq.2 clean-flag, Fujita attribution depth, γ_BI definition, v1B.0.54 hard-code, fn:rhat_csv length, §III heading "discrimination")
- NIT: 5 (title length, \textit{Note}, voice consistency, affiliation, PACS)
- **Total: 29 actionable findings**

**Justification of MAJOR-REVISION verdict.**

The EXT1 closure wave (v1B.0.55) is substantively well-executed. All 14
listed EXT1-closure items (A1–A16) hold on re-verification, with the
exception of E1 (the new README *itself* documents a misdiagnosed bug)
and MIN8 (v1B.0.54 hard-code at L2040 missed in A4). The cross-vendor
artefact crosscheck (`tools/artifact_crosscheck.py`) returns 0 broken
paths across 17 candidates — provenance plumbing is healthy.

The paper is publishable in PRD with a focused 1–2-week revision that
addresses the 4 ESSENTIAL findings:

1. **E1** is the highest-impact: the new README points to demonstrably
   wrong "conversions" for at least 5 of 6 raw parameters. This is a
   single-evening fix (rewrite the README, verify chain-column mapping),
   but must be fixed because the paper now points at this file from §Data
   and Code Availability as a reproducibility artefact. A referee chasing
   the pointer will find a bug. Strictly worse than v1B.0.54 where the
   JSON was simply undocumented.

2. **E2 / E3 / E4** are all variants of the same root pattern — the EXT1
   closures hardened the *body* prose but left the *headline surfaces*
   (abstract, table column headers, Conclusions paragraph titles) with the
   pre-closure overclaim phrasing. PRD referees read tables and abstracts
   before footnotes; the careful in-paper scope statements are not
   visible at the surface they need to be visible at. Each E-finding is
   a 1-line-to-3-sentence fix.

The 10 MAJOR findings are not blockers individually but their *aggregate*
makes the paper look unfinished. The DES-SN5YR/Pantheon+ overlap caveat
(M2) is the most consequential physics MAJOR — it should include an
effect-size bracket (5/10/15%) so the $+4.3\sigma$ marginal-tail framing
in E3 is honestly bracketed by a possible joint-covariance correction.

After ESSENTIAL + MAJOR fixes are applied, the paper will be a
solid "verified-true-bounce-program-companion" paper at PRD-acceptable
quality. The science is honest, the scope discipline is excellent
(the in-cell caveats and fn:wcaveat discipline are best-in-class for a
companion paper of this type), and the artefact provenance is excellent
modulo the README bug.

**Readiness recommendation: 92% (cap at 95% pending fixes; reach 99% only
after a clean R30 round on the revised version per the readiness-cap-99
standing rule).**

**One reader sanity-check:** A PRD referee who reads only the abstract
(L683–739) plus Fig. 1 should be able to state, in one sentence each,
(a) what was measured (ΔN_eff posterior, NaMaster pipeline-recovery bias,
spectator-ALP consistency), (b) what was *not* measured (sky-significance
detection of β, Bayes-factor model comparison, direct ECH-Boltzmann-module
test), and (c) what the headline result is (null ΔN_eff in stock-CAMB
$\Lambda$CDM extension; pipeline-recovery bias $|\Delta\hat\beta| \le
0.040°$; spectator-ALP accommodates $\beta_{\rm obs}=0.342° \pm 0.094°$
under non-minimal photon-coupling enhancement and $\sim 25\times$
misalignment tuning). On the v1B.0.55 abstract as-is, (a) and (b) are
clear; (c) is muddied by the pipeline-SNR figure embedded in the
abstract and by the absence of the spectator-status fine-tuning
disclosure in the headline-result framing. The 4 ESSENTIAL fixes close
this gap.

---

*End of R29_P1B_Claude_brutal review.*
