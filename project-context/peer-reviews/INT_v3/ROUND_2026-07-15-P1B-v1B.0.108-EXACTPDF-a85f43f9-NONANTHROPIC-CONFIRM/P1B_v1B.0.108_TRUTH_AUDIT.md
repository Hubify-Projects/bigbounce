# P1B v1B.0.108 exact-PDF three-leg truth audit

## Scope and provenance

- Exact reviewed PDF: `arxiv/paper1b_mcmc_companion.pdf`, SHA-256
  `a85f43f93ed7bb53e73304cd21fb0fe68ed0d6627103ccbcf970036d31d9a9fb`,
  19 pages.
- Review repository head: `bbdc79db20500e6aa64f2d6f246120a01c53d2bb`.
- Paper/source closure commit: `97ceca7f524044427b991d27244e35585a5b2a58`.
- Direct-provider board: Grok 4.3 **ACCEPT**; Gemini 3.1 Pro Preview
  **REJECT**. These verdict words are recorded as returned; neither is treated
  as journal acceptance or as a substitute for finding-level adjudication.
- The director explicitly authorized this one confirmation despite the prior
  anti-loop stop because the persistent goal requires a post-v1B.0.108 review.
- Comparison sources: the v1B.0.107 truth audit in the preceding exact-PDF
  round and the retained P1U ledger at
  `project-context/peer-reviews/DISPOSITIONS/P1U.md`.

## Finding-by-finding adjudication

### Grok 1 — torsion energy-density scale juxtaposed with the proxy bound

**Disposition: existing D-id/reflag (DP1U-15) plus unsupported-as-a-defect.**

The manuscript does place the parametric contact-energy scale beside the
stock-CAMB proxy sensitivity for scale context (`arxiv/paper1b_mcmc_companion.tex:1323-1331`).
It also explicitly says the ratio is *not* a predicted `Delta N_eff`, explains
that a numerical conversion requires a specified thermal spin ensemble and
prefactor, and refuses to claim a nonzero torsion `Delta N_eff`
(`arxiv/paper1b_mcmc_companion.tex:1729-1737`). The subsequent comparison is
identified as a generic proxy and says agreement between two null-sized
quantities is not theory evidence (`arxiv/paper1b_mcmc_companion.tex:1739-1744`).
Thus the missing conversion factor is not an omitted known calculation; it is
an explicitly declared modeling boundary. This is the same stock-CAMB-proxy /
not-an-ECH-test class recorded as DP1U-15, not a new correctness defect.

### Grok 2 — percentages might be mistaken for evidence/model probabilities

**Disposition: unsupported/stale; optional wording only.**

The prior-predictive draws are expressly unconditional and unweighted
(`arxiv/paper1b_mcmc_companion.tex:2421-2437`). The abstract says the 11.6% and
6.1% values are prior-sensitivity fractions, not a cost or probability of the
spectator subset (`arxiv/paper1b_mcmc_companion.tex:1341-1348`). The active body
repeatedly says the 13.3818% value is neither a physical posterior probability
nor a prior cost (`arxiv/paper1b_mcmc_companion.tex:2444-2451`,
`:2763-2768`, `:2926-2932`), and the likelihood appendix repeats the limitation
(`:3245-3254`). Adding the exact phrase “not Bayesian evidence” could improve
reader ergonomics, but the prohibited interpretation is already stated; no
scientific correction is required.

### Grok 3 — manifest does not pin the LFS payload OIDs to an exact commit

**Disposition: existing D-id/reflag (DP1U-16) and immutable-release gate, not a
new artifact-integrity failure.**

The manuscript accurately marks v1B.0.108 as pre-release and says the eventual
submission commit/tag will freeze source, manifest, and PDF together
(`arxiv/paper1b_mcmc_companion.tex:2962-2970`). It distinguishes pointer hashes
from payload OIDs/sizes and names the payload mirror (`:2971-2979`). The
v1B.0.108 changelog pins science commit `97ceca7f`, the manifest, all three
HuggingFace mirrors, and the exact PDF hash (`CHANGELOG.md:19-42`); Git tree
inspection confirms that commit contains the TeX, PDF, and manifest. The JSON
manifest intentionally records its pre-release base context rather than a
self-referential future release commit. An immutable public tag/DOI remains a
real release gate, already covered by DP1U-16, but the current provenance claim
is accurate.

### Gemini 1 — insufficient standalone scientific significance

**Disposition: venue-scope judgment; existing DP1U-15/DP1U-16 class.**

Gemini correctly observes that the paper disclaims a distinctive ECH test. The
abstract says none of the three exercises measures torsion or supplies evidence
for ECH/bounce cosmology (`arxiv/paper1b_mcmc_companion.tex:1315-1321`), and the
conclusion repeats the precise proxy/pipeline/accommodation scope (`:2877-2889`).
That honesty supports content correctness but can weaken fit as a standalone
JCAP research article. Whether a reproducibility and scope-control companion is
publishable standalone, supplementary, or better merged is an editor/human-
referee venue decision. It does not falsify the numerical claims.

### Gemini 2 — no standalone methodological novelty

**Disposition: venue-scope/novelty judgment, not a correctness finding.**

The paper does not claim to invent CAMB, Cobaya, NaMaster, or the scalar ODE. It
claims a frozen, reproducible three-part verification package and quantitative
scope control (`arxiv/paper1b_mcmc_companion.tex:1350-1352`). The exact-window
operator, robustness suite, prior-predictive calculation, and 195-artifact
manifest can be useful technical contributions without constituting a new
general algorithm. Gemini's view that JCAP requires a novel method is a
plausible venue-fit objection, but it is not evidence that an estimator, result,
or derivation is wrong.

### Gemini 3 — NaMaster check is trivial and carries no real-sky weight

**Disposition: existing D-id/reflag (DP1U-15) plus venue-value judgment; one
reviewer characterization is unsupported.**

The source agrees with the essential limitation: skies are foreground-free,
the beta/alpha calibration degeneracy is not broken, and the result is neither
a real-sky detection nor a systematic floor
(`arxiv/paper1b_mcmc_companion.tex:1333-1339`, `:2085-2097`, `:2917-2924`).
This maps directly to DP1U-15. Gemini's phrase “noise-only synthetic skies” is
not accurate: the test uses synthetic Lambda-CDM polarization signal plus stated
white noise, not noise-only maps (`:2031-2040`, `:2130-2168`). Whether exact
window-operator recovery and robustness are substantial enough for standalone
publication is a venue-value judgment. No new numerical error is identified.

### Gemini 4 — one-dimensional ALP summary likelihood

**Disposition: existing disclosed DP1U-15 scope limitation, with one
genuinely-new real MINOR overstatement in the active discussion.**

Gemini is correct that the fit uses a one-dimensional Gaussian summary rather
than the full `EB` likelihood. The manuscript states this directly
(`arxiv/paper1b_mcmc_companion.tex:2585-2604`, `:3237-3244`), describes the
constant-product degeneracy, and limits the result to accommodation rather than
prediction (`:2823-2840`, `:2926-2949`). Therefore the main criticism is an
existing disclosed limitation, not a newly discovered failure of the reported
conditional fit.

However, the active appendix goes beyond the available evidence when it says a
full joint-`EB` likelihood would “principally” reweight width/tails rather than
move the central location, calls the medians comparatively insensitive, and
predicts the shift will remain within the quoted 16–84% ranges
(`arxiv/paper1b_mcmc_companion.tex:3245-3259`). No full-`EB` reanalysis or
response calculation is supplied to establish those forecasts. This is a
genuinely-new, bounded **MINOR**: delete or weaken those prospective assertions
to “the direction and size of any shift require a full joint-EB refit.” It does
not invalidate the explicitly conditional summary-likelihood numbers.

## Content correctness versus JCAP fit

The direct reviews expose no new error in the stock-CAMB posteriors, exact-window
NaMaster recovery numbers, prior-predictive fractions, or conditional ALP-chain
summaries. Grok supports the central bounded claim. Gemini also says the
computational artifacts technically support the central reproducibility and
consistency claims, while rejecting the manuscript as a standalone JCAP article
for significance/novelty reasons. Those are different questions: the content is
largely correct within its declared scope; standalone JCAP suitability remains
unresolved and human/editorial.

## Direct-provider disposition

- **Genuinely-new real:** one MINOR—the unsupported forecast of how a full
  joint-`EB` likelihood would shift the ALP posterior (`:3245-3259`).
- **Existing disclosed/reflagged:** torsion-vs-proxy scale context, synthetic
  NaMaster evidentiary limits, summary-likelihood limitation, and provenance /
  immutable-release status (DP1U-15/DP1U-16).
- **Venue-scope judgments:** standalone significance, methodological novelty,
  and merge/supplement disposition.
- **Unsupported/stale reviewer claims:** a required known `Delta N_eff`
  conversion is absent; percentages are not already disclaimed; the skies are
  noise-only; current pre-release provenance falsely claims an immutable tag.

The exact v1B.0.108 artifact should not be labeled accepted or JCAP-ready from
this two-leg board. A bounded one-sentence closure of the full-`EB` forecast is
scientifically justified; further automated wording churn on the venue disputes
is not.

## Codex subscription addendum

### Binding and modality

The subscription-backed Codex CLI leg reviewed the same 19-page PDF SHA-256
`a85f43f93ed7bb53e73304cd21fb0fe68ed0d6627103ccbcf970036d31d9a9fb`
and source SHA-256
`d65b8150655881d852c440030fc65f1cf323152bc50a4a747412236c6767a9d4`
from a clean detached sparse tree at
`6534a6e8fc57419f1674df4ee5dd13adad19854b`. Authentication was through
the ChatGPT subscription, not the OpenAI API. Its verdict was **MAJOR
REVISIONS** with two MAJOR and four MINOR findings.

### Codex 1 — standalone JCAP venue fit

**Disposition: venue-scope judgment; confirmed as distinct from scientific
correctness.**

This is the same issue as Gemini 1–2 above. Codex accurately cites the paper's
own statement that the three analyses are disconnected, bounded proxy /
validation / accommodation studies (`arxiv/paper1b_mcmc_companion.tex:1509-1521`,
`:1648-1662`, `:2085-2097`, `:2395-2420`, `:2877-2889`). Its demand for one
coherent new cosmological question or a broadly benchmarked new method is a
credible JCAP editorial standard, not a reproduced numerical error. Closure is
a human venue/form decision: standalone JCAP research article versus technical
note/supplement/merge with P1A.

### Codex 2 — unconditional prior predictive versus spectator condition

**Disposition: genuinely-new REAL / MAJOR interpretation defect; unconditional
numbers remain numerically valid.**

The committed prior-predictive code samples the stated unrestricted priors and
computes only `beta`; it neither computes nor imposes `Omega_a < 0.01`
(`reproducibility/cosmology/alp_prior_predictive.py:122-185`). The manuscript
does disclose that the 11.597% / 6.137% values are unconditional and unweighted
(`arxiv/paper1b_mcmc_companion.tex:2421-2437`) and separately explains that the
spectator-safe inference requires `Omega_a < 0.01` (`:2439-2452`). Thus the
published percentages are correct for the unrestricted fixed-background ALP
prior, but they are not spectator-conditioned accommodation fractions.

A read-only deterministic audit diagnostic propagated 10,000 seed-1234 draws
per arm through the same DOP853 equations while also evaluating the committed
today-energy formula. The fast/reference cross-check over 20 random draws gave
maximum discrepancies `2.54e-8 deg` in `beta` and `1.05e-6` in `Omega_a`.
Results were:

- broad `C_agamma ~ U[4,60]`: unconditional 1-sigma fraction 5.73%;
  `Omega_a<0.01` prior fraction 35.65%; joint band-and-spectator fraction 0.68%;
  conditional band fraction 1.907% (68/3,565; binomial SE 0.229 percentage
  points);
- fixed `C_agamma=8`: unconditional 1-sigma fraction 11.80%;
  `Omega_a<0.01` prior fraction 35.65%; joint and conditional band fractions
  0/10,000 and 0/3,565 in this diagnostic (the zero is not asserted as an exact
  population probability).

The 10,000-draw values are an audit diagnostic, not a replacement publication
artifact; their unconditional values agree with the committed 100,000-draw
values at Monte Carlo scale. They establish that spectator conditioning changes
the scientific interpretation materially. Closure requires either (a) rename
the reported values everywhere as **unrestricted fixed-background ALP**
prior-predictive fractions and never use them to characterize the spectator
model, or (b) run and archive the full pre-specified 100,000-draw
spectator-conditioned calculation (and, ultimately, a self-consistent
background for draws outside the spectator regime). This is the board's only
new MAJOR scientific-interpretation finding.

### Codex 3 — NaMaster recovery grid

**Disposition: genuinely-new REAL / MINOR reproducibility mismatch.**

The manuscript says `[-2,+2] deg` at `0.001 deg` spacing
(`arxiv/paper1b_mcmc_companion.tex:2173-2177`). The executed production calls
use `recover_beta_deg(...)` without a grid override
(`reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py:259-268`), whose
default is `np.linspace(-1.0,1.0,2001)`
(`reproducibility/p1_namaster_500mc/scripts/windowed_rotation.py:65-68`). The
spacing is still exactly `0.001 deg`, and all reported injections lie well
inside the executed range, so the recovery numbers are unchanged. Closure:
change only the manuscript range/count to `[-1,+1] deg`, 2,001 grid points.

### Codex 4 — S8 overlap grid

**Disposition: genuinely-new REAL / MINOR reproducibility mismatch.**

The manuscript states a `Delta S8=1e-4` grid on `[0.70,0.90]`
(`arxiv/paper1b_mcmc_companion.tex:1897-1902`). The committed calculation uses
`np.linspace(0.70,0.92,4001)`, hence exact spacing `0.22/4000 = 5.5e-5`
(`reproducibility/cosmology/c13_s8_desy3_overlay.py:80-89`). The displayed
overlap values remain unchanged at quoted precision. Closure: update the
manuscript recipe to 4,001 points, `[0.70,0.92]`, `Delta S8=5.5e-5`.

### Codex 5 — fixed-coupling theta and mass summary convention

**Disposition: genuinely-new REAL / MINOR labeling/rounding mismatch.**

Direct read-only recomputation from
`research/branch_R_alp_birefringence/phase2_mcmc/chains/run1_full/alp.1.txt`
gives 2,160 rows with multiplicity-weight sum 8,715. Multiplicity-weighted
`theta_i` is mean +/- population SD `1.35943 +/- 0.44883`; its weighted
16/50/84 percentiles are `0.94815 / 1.31684 / 1.75609`, or median
`1.31684^{+0.43925}_{-0.36869}`. The source's `1.32 +/- 0.41`
(`arxiv/paper1b_mcmc_companion.tex:2593-2594`, `:3177-3178`) therefore mixes a
median-like centre with an approximately symmetrized central interval while
using mean-plus/minus-SD notation. The weighted log-mass median is `-31.271087`,
which with the stated `H0=1.44e-33 eV` gives `m/H0=37.20065`, not 36 exactly.
Both differences are small and do not alter `m >> H0`. Closure: choose and name
one convention—prefer the asymmetric median interval above—and report mass as
`37.2 H0` (or explicitly label 36 as coarse historical rounding).

### Codex 6 — immutable release

**Disposition: REAL release/provenance gate, already disclosed (DP1U-16), not
a new content defect.**

The exact PDF/source/manifest are commit-bound locally, but the paper truthfully
labels the package pre-release, uses mutable `main` URLs, and leaves the final
tag/DOI pending (`arxiv/paper1b_mcmc_companion.tex:2962-2997`, `:3069-3112`).
Acceptance requires an immutable public release binding source, PDF, code,
manifest, and LFS payload identifiers. Closure is release engineering, not a
manuscript-number correction.

## Complete three-leg board disposition

- Grok: **ACCEPT**, with no surviving new correction after audit.
- Gemini: **REJECT**, principally standalone JCAP significance/novelty; one
  bounded real MINOR survives for the unsupported full-`EB` posterior-shift
  forecast.
- Codex subscription: **MAJOR REVISIONS**; one real MAJOR interpretation issue
  (unconditional versus spectator-conditioned prior predictive), three real
  MINOR recipe/summary mismatches (NaMaster grid, S8 grid, theta/mass convention),
  one venue judgment, and one immutable-release gate.

The limited stock-CAMB and exact-window NaMaster numerical results remain
supported. P1B v1B.0.108 is not yet acceptance-ready: close the one MAJOR and
four MINOR source issues, then build the immutable release; standalone JCAP fit
still requires a human/editorial decision.
