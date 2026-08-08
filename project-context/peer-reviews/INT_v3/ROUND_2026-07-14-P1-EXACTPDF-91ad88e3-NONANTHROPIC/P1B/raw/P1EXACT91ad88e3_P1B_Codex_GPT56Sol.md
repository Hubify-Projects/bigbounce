## Overall assessment

P1B contains a credible null MCMC result and several unusually well-preserved numerical artifacts. The stock-CAMB \(\Delta N_{\rm eff}\) results, truncation treatment, sample accounting, birefringence normalization, LiteBIRD forecast formula, Figure 2 labeling, chain cuts, and prior-predictive calculations all check.

The frozen manuscript is nevertheless not acceptable in its current form. Two consequential issues alter the interpretation of headline results: the ALP “posterior mass/prior cost” is normalized over a surrogate chain containing physically inconsistent points, and the NaMaster recovery test compares bandpowers against an incorrectly sampled rather than consistently binned theory template. These do not erase the verified null MCMC or artifact-level results, but they prevent the affected ALP and synthetic-pipeline conclusions from being stated as presently written.

## Findings

### P1B-E1 — ALP posterior normalization is not physically valid

**Severity:** Blocker  
**Type:** Real technical defect

The ALP likelihood holds the background fixed to \(\Lambda\)CDM and never feeds the derived \(\Omega_a\) into \(H(z)\). This approximation is internally inconsistent for the substantial chain support at \(\Omega_a\sim0.1\)–1.

The \(\Omega_a<0.01\) samples themselves lie within the stated spectator regime, but the reported 13% fraction is normalized by a full-chain denominator dominated by points outside that regime. Consequently:

- \(13.3818\%\) is an exact diagnostic survival fraction of the surrogate chain.
- It is not a defensible physical posterior probability or “prior cost.”
- The analogous \(44.0474\%\) fraction for \(\Omega_a<0.1\) has the same normalization caveat.

Closure requires either a background-consistent likelihood over the relevant support or removal of the posterior-probability/prior-cost interpretation. The fractions may remain as explicitly labeled surrogate-chain validity diagnostics.

### P1B-E2 — Theory and recovered NaMaster bandpowers are mismatched

**Severity:** Blocker  
**Type:** Real technical defect

The estimator constructs decoupled broad bandpowers but fits them to \(C_\ell^{EE}\) evaluated at each bin’s effective center. The theory must instead be passed through the same bandpower window/binning operator used for the recovered spectrum.

This mismatch can itself generate a multiplicative recovery bias. The existing robustness tests vary weights, \(\ell_{\max}\), BB templates, masks, and apodization, but none tests the missing theory-window operation. Therefore:

- The observed \(\sim12\%\) bias cannot presently be attributed mainly to unweighted noise-dominated bins.
- The quoted \(0.040^\circ\) value cannot yet be promoted as a pipeline or systematic floor.
- The raw synthetic recovery values remain valid descriptions of the current estimator implementation, not validated real-sky performance.

A correctly windowed-theory rerun is required before interpreting the bias or retaining the floor.

### P1B-M1 — The stated reproducibility snapshot is not the reviewed version

**Severity:** Major  
**Type:** Reproducibility defect

The manuscript identifies commit `b22f8cc9` as the matching current snapshot, but that commit contains v1B.0.47. The reviewed manuscript is v1B.0.105 at exact commit `91ad88e36121da128175415f55be44d5e458f9f1`.

The paper must identify an exact commit containing the submitted source, tables, figures, chains, scripts, and supporting artifacts. This is not submission metadata or venue taste; it is a verified provenance failure.

### P1B-M2 — Table IV mixes stale statistics and unsupported ESS provenance

**Severity:** Major  
**Type:** Real table and reproducibility defect

Exact weighted chain statistics give:

| Selection | Exact \(\beta\) mean | Std. dev. | Median | Manuscript |
|---|---:|---:|---:|---|
| Full | 0.32629 | 0.09899 | — | \(0.326\pm0.099\), correct |
| \(\Omega_a<0.1\) | 0.31471 | 0.10258 | 0.31909 | \(0.328\pm0.100\), inconsistent |
| \(\Omega_a<0.01\) | 0.27595 | 0.09880 | 0.28409 | \(0.28\pm0.10\), acceptable rounding |

The caption/heading describes \(\beta\) entries as medians even though at least the full-chain value is a mean. ESS entries also mix marker parameters or estimators without identifying them. A weight-expanded Sokal-style check gives approximately:

- Full: \(\mathrm{ESS}_\beta=2937\), \(\mathrm{ESS}_\theta=812\)
- \(\Omega_a<0.1\): \(\mathrm{ESS}_\beta=1530\), while an alternative \(w_a\)-like marker gives about 1935; manuscript: 1989
- \(\Omega_a<0.01\): \(\mathrm{ESS}_\beta=491\); manuscript: 461

No compact committed script or artifact reproduces 1989 and 461. Table IV must be regenerated from one declared statistic, marker, weighting convention, and committed script. This defect does not make the 44% and 13% weighted cut fractions arithmetically false.

### P1B-m1 — One convergence statement exceeds the manuscript’s convention

**Severity:** Minor  
**Type:** Real technical reporting defect

The c15 chain has \(R-1=0.0147\), exceeding the paper’s stated \(<0.01\) convention. It is honestly non-headline, but should be flagged as not satisfying that threshold rather than implicitly grouped with converged headline chains.

### P1B-m2 — “Propagating torsion” is inaccurate for minimal ECH

**Severity:** Minor  
**Type:** Real technical wording defect

Minimal Einstein–Cartan–Holst torsion is algebraic rather than a propagating degree of freedom. “Propagating torsion” must be removed or explicitly attributed to a specified UV completion with additional dynamics.

### P1B-m3 — Statistical and systematic terminology needs normalization

**Severity:** Minor  
**Type:** Real reporting defect

The revision should:

- distinguish means from medians consistently;
- define every SNR convention where used;
- identify the ESS marker and estimator;
- call \(0.040^\circ\) a synthetic-estimator result unless and until the corrected recovery test supports stronger language;
- avoid presenting synthetic recovery performance as a real-sky systematic floor.

### P1B-N1 — Verified numerical results are not findings against the paper

**Severity:** No defect  
**Type:** Verified result

The following checks pass:

- Stock-CAMB \(\Delta N_{\rm eff}\) means and errors.
- One-sided truncation procedure.
- Sample-count reconciliation.
- Estimator normalization \(\tfrac12\sin(4\beta)\).
- LiteBIRD uncertainty formula.
- Figure 2 \(\Delta N_{\rm eff}\) label.

Direct-vendor objections contradicting these results are stale or based on misreading.

### P1B-N2 — Additional analysis requests are disclosed-scope questions

**Severity:** No automatic defect  
**Type:** Disclosed limitation

New noise levels, optional alternative bin ranges beyond correcting the actual template mismatch, or otherwise identical likelihood reruns are potentially useful extensions. They are not independently required unless the manuscript makes claims needing them.

### P1B-N3 — Venue and submission issues must remain separate

**Severity:** No scientific defect  
**Type:** Venue opinion or submission metadata

Novelty, manuscript length, and AI-disclosure preferences are venue judgments. DOI assignment and companion arXiv identifiers are submission metadata tasks. The three cited Hugging Face dataset URLs resolve successfully. None should be confused with the technical defects above.

## Exact-chain and artifact recomputations

For the frozen c5 chains:

- Rows: **8,955**
- Total Monte Carlo weight: **82,754**
- \(\Omega_a<0.1\): **44.0474%**
- \(\Omega_a<0.01\): **13.3818%**
- \(\theta_i\le0.1\): **0.32748%**

These cut fractions are arithmetically reproducible. Their physical interpretation remains subject to P1B-E1.

For the committed prior-predictive artifact, using 100,000 draws per configuration:

- Fixed coupling: **11.597%**
- Broad coupling: **6.137%**
- Integration failures: **0**
- Maximum integrator discrepancy: **\(2.49\times10^{-8}\) deg**

These results reproduce and should be retained.

## Final recommendation

**Major revision.** If the venue permits only a binary decision on this frozen version, the appropriate decision is reject with invitation to resubmit—not acceptance.

The manuscript’s core null-chain arithmetic and several central technical checks survive. Rejection on fundamental invalidity would therefore be disproportionate. However, acceptance would also be unjustified: the ALP posterior interpretation and NaMaster pipeline-floor interpretation require substantive correction, while the provenance and Table IV defects prevent exact reproduction of the submitted claims.

## Genuinely new blockers only

- Correct the ALP surrogate-chain normalization or remove all physical posterior-mass/prior-cost interpretation from the 44% and 13% fractions.
- Rerun the synthetic recovery with theory passed through the identical NaMaster bandpower window/binning operator before interpreting the \(\sim12\%\) bias or \(0.040^\circ\) floor.
- Replace the mismatched `b22f8cc9` provenance claim with an exact, complete snapshot of v1B.0.105 and its artifacts.
- Regenerate Table IV from a committed script with consistent mean/median definitions and explicitly declared ESS marker and estimator.