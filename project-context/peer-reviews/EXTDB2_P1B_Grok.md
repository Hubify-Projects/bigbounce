# EXTDB2 P1B Grok — chat: https://grok.com/c/2a3cddfc-4561-48a0-8667-8655b3fdb99c?rid=29fc075a-ec23-4393-8f0c-3b862eb07427

Provider: Grok Expert
PDF md5: dbf1d9d374f4923fd33c7e30cbd36ad5
Harvested: 2026-06-28

---

Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program (Paper P1B)
Manuscript: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+∆Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
Author: Houston Golden
Date: June 27, 2026

Recommendation: MINOR REVISIONS

Summary of paper: This is a technical companion to the structural no-go analysis of minimal Einstein-Cartan-Holst (ECH) spin-torsion dark-energy routes in Paper I(a). It reports three scoped verification analyses on stock CAMB (no torsion modifications): (1) a ΛCDM+∆Neff MCMC proxy (~309k frozen samples across two converged dataset combinations); (2) a 500-realization NaMaster pseudo-Cℓ Monte Carlo pipeline validation on synthetic foreground-free ΛCDM polarization skies with injected birefringence angles; and (3) a standard-GR spectator-ALP consistency check (MCMC on published Eskilt & Komatsu β=0.342°±0.094° summary likelihood). All three are framed explicitly as compatibility checks only; no claim of evidence for/against bounce cosmology, direct ECH module testing, sky detection, or distinctive ECH prediction.

BLOCKERS: None. No mathematical errors, false claims, missing critical controls that invalidate core conclusions, or unaddressed systematics. The paper is unusually careful in scope statements, caveats, and what it does not claim.

MAJORS: None that rise to the level of blocking acceptance or requiring new calculations/reruns. The analyses are technically sound within their explicitly stated scopes.

MINORS:

1. w0wa cross-check (Sec. V.C and Table II) — uncontrolled SN-overlap systematic and presentational risk. The iter2 DESI DR2 + Planck NPIPE + DES-Y5 + Pantheon+ chain (overlap-uncorrected product likelihood) shows a phantom-crossing posterior (w0+wa≈−1.48) with marginal-tail extrapolation distances quoted as +4.3σ (w0) and −3.6σ (wa). These are correctly flagged as "diagnostic only — not detection significances," "inflated by the uncorrected ~20% shared-event Malmquist difference," and with model-selection explicitly deferred because the ΛCDM point is unsampled. However, presenting quantitative σ-distances alongside an acknowledged dominant uncontrolled systematic risks reader misinterpretation. The two planned overlap-control chains are noted as deferred to a follow-up note.
   Suggested revision: Either (a) move the quantitative σ-distances and Table II to supplementary material with a one-paragraph summary emphasizing the qualitative quintom-B direction under the stated caveat, or (b) add a short explicit statement at the opening of V.C that this cross-check is included for completeness as an exploratory diagnostic (distinct from the minimal matter-bounce fNL=−35/8 prediction of P1a) but does not alter the primary compatibility conclusions.

2. Linkage between the three analyses and the P1a no-go results. A short explicit paragraph (perhaps in Sec. I or a new "Relation to Paper I(a)" subsection) would strengthen the companion framing: why these three checks specifically (∆Neff proxy tests whether data require extra radiation that minimal matter-bounce does not produce; NaMaster validates the tool underlying published birefringence constraints; ALP shows the observed signal is accommodable in standard GR but requires disclosed tunings independent of the gravitational theory).

3. Minor presentational tightenings (non-blocking):
   - In the abstract and Sec. VI, the spectator-ALP tuning (~25× misalignment relative to natural-prior midpoint for θi~0.1 to achieve Ωa<0.01) is already disclosed; a single additional clause noting this tuning is required regardless of whether the background is bounce or ΛCDM would reinforce the "not distinctive ECH" point.
   - The long sample-count/burn-in reconciliation footnotes in Sec. III are valuable but disrupt flow; consider moving the most arithmetic-heavy parts to Appendix A while retaining the headline reconciliation statement.
   - Ensure that the final published version cross-references the exact commit/SHA or in-text version stamp (v1B.0.79) consistently between the PDF and the GitHub/HuggingFace artifacts.

STRENGTHS:

1. Exceptional, load-bearing scoping and caveat discipline. The paper repeatedly and explicitly states what each analysis is not (not a direct ECH spin-torsion Boltzmann test; not a competitive sky detection; not evidence for/against bounce; ALP birefringence not distinctive to ECH; spectator status requires disclosed fine-tuning of misalignment; model preference deferred). Such discipline is rare and directly addresses the high bar for interpretive overreach in cosmological extensions.

2. Reproducibility and transparency at gold-standard level. Public version-stamped GitHub repository with all Cobaya YAMLs, NaMaster driver scripts, EOM integration code, IMPLEMENTATION MAP.md, and frozen chains on HuggingFace; detailed Appendix A reproducibility manifest; independent pod re-run cross-check for the ∆Neff proxy (0.04σ agreement under release-pairing swap); explicit disclosure of legacy JSON column-index bug and burn-in arithmetic.

3. Rigorous empirical robustness and bias attribution rather than assumption of ideality. For the NaMaster validation: full sky-fraction sweep (fsky=0.32/0.65/0.85), sign-symmetric negative-β injection, apodization-scale variations, purification on/off, estimator weighting (unweighted vs. inverse-variance), BB template shape variations, and independent local rerun. Bias is quantified empirically (−0.032° to −0.040° worst-case) and attributed to specific sources rather than claimed unbiased.

4. Honest, non-overinterpreted null/consistency results with physical one-sided limits. ∆Neff consistent with zero; H0 tension with SH0ES persists at ~3.6σ; ALP posterior accommodates observed β but shifts to m≫H0 with quantified spectator-subset mass (13% at Ωa<0.01) and coupling burden outside minimal KSVZ/DFSZ benchmarks. No claim is made that these resolve tensions or favor ECH.

5. Clear separation of pipeline-validation figures from sky-measurement significances.
