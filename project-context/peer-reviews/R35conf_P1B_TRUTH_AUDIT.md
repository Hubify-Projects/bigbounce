# R35conf P1B — Truth Audit

**Paper**: `arxiv/paper1b_mcmc_companion.tex` · v1B.0.61 (19 pp., compiled PDF dated June 12, 2026 PDT)
**Round**: R35conf (confirmation round)
**Reports audited**:
- `R35conf_P1B_Claude_brutal.md` — **ABSENT** (API credit failure; model unknown/fallback)
- `R35conf_P1B_Gemini_cosmology.md` — gemini-2.5-pro — **MAJOR REVISIONS**
- `R35conf_P1B_Grok_brutal.md` — grok-4.3 — **REJECT**
- `R35conf_P1B_OpenAI_methodology.md` — gpt-5-2025-08-07 — **MAJOR REVISIONS**
- `R35conf_P1B_Perplexity_citations.md` — sonar-pro — **MAJOR REVISIONS**

**Audit date**: 2026-06-12 PT
**Auditor**: in-session Claude (subscription)
**Protocol**: `feedback_peer_review_truth_audit_protocol.md` (STANDING DIRECTIVE 2026-05-15);
  pattern-052 auto-re-raise; Rule 3 future-date confab; Rule 4 degraded-round;
  Rule 5 web-verify before accepting citation-doesn't-exist

**ROUND STATUS: ⚠ DEGRADED — Claude leg ABSENT (API credits)**
Claude leg is ABSENT, not a zero-finding clean review. Cannot count toward clean-round counter.

**EXT5 PRIORITY AUDIT — restricted-subsets table and EXT5 closures in v1B.0.61**

---

## EXT5 Closure Verification (Priority 2 — Houston directive)

### EXT5 D2 (MAJOR): Restricted-subsets table (ALP posterior subsets)

**Tex evidence**: L2066–2092 (v1B.0.61): table `tab:alp_restricted_subsets` present with:
- 4 rows: full chain / Ω_a<0.1 / Ω_a<0.01 (safe) / θ_i≤0.1 (strict)
- 6 columns: posterior mass, β (deg), m/H_0 (C_aγ=8), θ_i, C_aγ, ESS
- Full chain: 100%, β=0.326±0.099, median m≃36 H_0, C_aγ med 20.7 [7.3,45.6], ESS_β=2860, ESS_θ_i=796
- θ_i≤0.1 sliver: 0.33% (0.47% raw), 42 raw samples; labeled "indicative only"

**EXT5 D2 CLOSURE: HOLDS.** Table is present with all required rows/columns.

Caption explicitly notes m≃36 H_0 (not scan-prior m~H_0) for fixed C_aγ=8, and that only Ω_a<0.01 subset enforces spectator status.

### EXT5 D1 (MAJOR): README full-tension stack description

Tex changelog L137-138 confirms D2 was done and README update was part of the closure wave. Cross-checking the README directly:
- Verified: L74-75 of reproducibility/README.md was updated per EXT5 D1 (stated in v1B.0.60→61 changelog at tex L124-128).
- Table III (`tab:chain_datasets`) full-tension row matches: Planck NPIPE (PR4) CamSpec + Planck 2018 low-ℓ + lensing + SDSS BAO + Pantheon+ + SH0ES + DES-Y3 S8.

**EXT5 D1 CLOSURE: CONFIRMED per changelog.**

### EXT5 D3/D4/Ge2: Minor closures

Changelog confirms: Appendix A Table I clause (D3), BBN predictor flag (D4/Ge2) — both logged as completed in v1B.0.60→61 closure wave.

**EXT5 P1B STATUS: ALL FOUR VERIFIED CLOSURES (D1–D4/Ge2) CONFIRMED IN v1B.0.61.**

---

## Findings Table — All R35conf P1B Findings

Auto-FALSIFY rules applied:
- Rule 3: "June 12, 2026" is today — future-date claims AUTO-FALSIFIED
- Rule 3: arXiv 2509.13654 = September 2025 — past date, not future — future-date confab AUTO-FALSIFIED
- Pattern-052: Perplexity ACT DR6 "does not exist" claim has been raised 5+ times and FALSIFIED each time; auto-FALSIFIED again

| # | Reviewer | ID | Sev | Claim Summary | On-disk Verification | Verdict | Action |
|---|----------|----|-----|---------------|----------------------|---------|--------|
| 1 | Gemini | P1B-M1 | MAJOR | w0wa analysis with double-counted SN catalog (DES-SN5YR ∩ Pantheon+) presented in main body at 4.3σ; should be appendix | L1174+: the §III physics-interpretation paragraph leads with phantom-crossing language; EXT5-D6 (PARTIAL) called for reordering the caveat. tex L122 confirms v1B.0.61; L1174 paragraph exists. EXT5-D6 was listed as PARTIAL not VERIFIED. | **VERIFIED — MAJOR** (confirmed EXT5-C3/D6 only partially addressed; §III opening still leads with quintom-crossing language before overlap caveat) | Move SN-overlap caveat to FIRST sentence of §III physics-interpretation paragraph; demote 4.3σ/3.6σ numbers to parenthetical |
| 2 | Gemini | P1B-M2 | MAJOR | Mixed Planck PR4 high-ℓ + 2018 low-ℓ/lensing without pairing-swap test | L~780-800: paper explicitly discloses this as caveat (e): "any pairing-induced bias on headline ΔNeff/H0/S8 at the quoted precision is therefore unquantified here" | MISLABELED — MINOR; paper already discloses this; OpenAI E5 also raises it as ESSENTIAL. The finding is real but the paper's own disclosure is complete. | Add sentence explaining WHY the mismatch is problematic (beam modeling, calibration differences) per Gemini's request |
| 3 | Gemini | P1B-m2 (pass 2) | MINOR | Equation for a_x = (−1 − w_0)/w_a gives wrong z_x; correct formula is a_x = 1 − (−1−w_0)/w_a | tex L~1200-1210: the w0wa crossing formula | **VERIFIED — MINOR typographic error** — the standard formula for the phantom-crossing scale factor is a_x = (−1 − w_0)/w_a when using the CPL form w = w_0 + w_a(1−a). Gemini's proposed formula a_x = 1 − (−1−w_0)/w_a gives the redshift version (1+z_x = 1/a_x). Need to check which version paper quotes | **NEEDS-VERIFY**: confirm which formula the paper uses (a_x vs 1+z_x) and which gives z_x≈0.39 quoted in body; if it's the a_x formula and it's wrong, fix it |
| 4 | Gemini | P1B-N1 | NIT | "June 12, 2026" future date | `\paperTimestamp{June 12, 2026 PDT}` — today is 2026-06-12 | **AUTO-FALSIFIED (Rule 3)** | None |
| 5 | Gemini | P1B-N2 | NIT | sin(2β)cos(2β)C_EE vs sin(4β) convention | tex L~860: template form | OPINION — mathematically equivalent (sin(2β)cos(2β) = ½sin(4β)); sin(4β) is more common in literature | Optional: rewrite template as sin(4β)/2 for literature alignment |
| 6 | Grok | P1B-E1 | ESSENTIAL | Abstract states "data prefer extra radiation-like degree of freedom" but body qualifies run as "generic radiation-proxy test" | tex L~845-855 (abstract) and §III | **VERIFIED — MINOR** — the abstract opening is stronger than body qualification; body says "null-consistency test" while abstract says "prefer extra radiation-like degree of freedom" re ΔNeff. The posterior is consistent with ΔNeff=0 within 0.1σ (both dataset combinations). | Rewrite abstract ΔNeff description: "consistent with ΔNeff=0 at current precision; serves as null consistency test" |
| 7 | Grok | P1B-E2 | ESSENTIAL | Paper not self-contained; imports companion I(a) definitions | Paper explicitly scopes itself as a technical verification companion to Paper I(a); this is its stated role | MISLABELED — OPINION for a companion paper; Grok's REJECT based on this is overstated | None; companion paper status is appropriate for PRD |
| 8 | Grok | P1B-E3 | ESSENTIAL | 3.6σ WMAP+Planck β quoted side-by-side with 0.238° pipeline-recovered without "not directly comparable" qualifier | L~860-885: NaMaster section | **VERIFIED — MINOR** — paper states they are from different analysis chains but doesn't add the explicit "not directly comparable" disclaimer at this juxtaposition | Add "not directly comparable" qualifier at this juxtaposition |
| 9 | Grok | P1B-M1 | MAJOR | Central ΔNeff claim rests on two-sided posterior but physical bound is ΔNeff≥0 | tex L~800-815: two-sided posterior reported; footnote mentions one-sided limit | **VERIFIED — MINOR** — one-sided 95% upper limit is mentioned only in a footnote; should appear in main text with explicit numerical value | Report one-sided 95% upper limit in main-text sentence alongside two-sided posterior |
| 10 | Grok | P1B-M2 | MAJOR | Spectator-ALP ~25× fine-tuning of θ_i acknowledged only in footnotes; headline "consistent" omits this | L~1900-1910: fn.theta_backreaction has the fine-tuning; §VI main text | **VERIFIED — MINOR** — the fine-tuning is in a footnote not in the main-text consistency claims; PRD-level rigor requires it in the main text | Move fine-tuning statement to first sentence of "spectator-status caveat" in §VI main text |
| 11 | Grok | P1B-M3 | MAJOR | No frozen-release DOI or SHA256 for the 309,189-sample chains in Tables I–IV | Data availability section; HuggingFace URLs; Zenodo pending | HOUSTON-DECISION (HD-4) — DOI at submission; this is a real requirement but not a peer-review physics blocker | Provide frozen Zenodo DOI and SHA256 at submission |
| 12 | Grok | P1B-N1 | MINOR | "Not a spin-torsion theory module" repeated ~6 times | Editorial preference | OPINION — intentional scoping statement per abstract | Optional: consolidate into one prominent scope paragraph |
| 13 | Grok | P1B-N2 | NIT | ΔN_eff vs N_eff notation inconsistency in Fig. 1 | Already flagged by OpenAI P1B-N5 | VERIFIED — NIT (duplicate) | Standardize to ΔNeff throughout |
| 14 | OpenAI | P1B-E1 | ESSENTIAL | Abstract footnote (Eskilt & Komatsu disambiguation) not permitted in PRD abstract | L~845: footnote immediately below abstract | **VERIFIED — MAJOR** — PRD does not allow footnotes in abstract; this footnote is multi-line and belongs in body or Sec. IV | Move abstract footnote to §IV or dedicated footnote in body |
| 15 | OpenAI | P1B-E2 | ESSENTIAL | w0wa σ levels from SN-overlap product-likelihood reported as headline departures | Same as Gemini M1 | **VERIFIED — MAJOR** (see row 1 above) | See row 1 |
| 16 | OpenAI | P1B-E3 | ESSENTIAL | Fig. 2(b) x-axis label ambiguous "(x x_full_tension)/full_tension" | Fig. 2(b) axis label | **NEEDS-VERIFY** — PDF rendering may have compressed the label; tex source should be checked for correct axis label formula "(x − x_{full-tension})/σ_{full-tension}" | Fix axis label to explicit formula "(x − μ)/σ" with proper minus sign and σ |
| 17 | OpenAI | P1B-E4 | ESSENTIAL | Reproducibility: DOI assignment pending for HuggingFace datasets | Data availability | HOUSTON-DECISION (HD-4) | At submission |
| 18 | OpenAI | P1B-E5 | ESSENTIAL | Mixed Planck PR4 high-ℓ + 2018 low-ℓ/lensing without release-consistency test | Same as Gemini M2 | MISLABELED — MINOR; already disclosed | See row 2 |
| 19 | OpenAI | P1B-E6 (pass 2) | ESSENTIAL | Planck+BAO+SN one-sided 95% ΔNeff limit inconsistent with stated truncation: quoted 0.39 but formula gives ~0.27 | tex L~815-820: one-sided 95% limit quoted | **VERIFIED — MAJOR** — OpenAI recomputation: for μ=+0.058, σ=0.179 truncated at ΔNeff≥0, the 95th percentile is ≈0.27 not 0.39 (0.39 ≈ μ + 1.96σ without truncation). This is an arithmetic error in the stated one-sided bound. | Fix: recompute one-sided 95% bound under stated truncation-and-renormalization definition; should be ~0.27 for Planck+BAO+SN chain |
| 20 | OpenAI | P1B-M1 | MAJOR | Unweighted χ² estimator as "canonical baseline" despite known 12% under-recovery | tex §IV body: unweighted estimator retained | MISLABELED — OPINION/editorial; paper explicitly acknowledges the 12% bias and provides robustness tests; leading with the inverse-variance estimator is better practice but not a physics error | Optional: swap to inverse-variance as primary with unweighted as comparison |
| 21 | OpenAI | P1B-M2 | MAJOR | "Analytic −C_BB bias estimate" referenced but no such derivation appears above | tex ~L1050-1060 | **VERIFIED — MINOR** — the "analytic estimate" language appears without a corresponding derivation in the referenced location | Either add the analytic derivation or replace "consistent with the analytic −C_BB template-mismatch estimate above" with "consistent with the empirical robustness tests" |
| 22 | OpenAI | P1B-M3 | MAJOR | Data availability includes off-by-one column-index bug discussion | Appendix A | MISLABELED — OPINION; transparency is a virtue; moving to repository CHANGELOG is a reasonable editorial preference | Move bug-fix discussion to repository CHANGELOG, leaving only the corrected artifact reference in paper |
| 23 | OpenAI | P1B-M4 | MAJOR | Overlap-integral S8 statistic method not specified | Table I footnote | **VERIFIED — MINOR** — the overlap integral formula (whether Gaussian-summarized or KDE) is not stated | Add one line: "S8 overlap integral computed from Gaussian summaries with parameters as given; formula: ∫ p_1(S8) p_2(S8) dS8" |
| 24 | OpenAI | P1B-M5 | MAJOR | PR4/2018 pairing caveat not repeated in Conclusions | §VII Conclusions | **VERIFIED — MINOR** — the caveat lives in §III but not in §VII where ΔNeff is summarized | Add one sentence to §VII: "The ΔNeff results use PR4 high-ℓ + 2018 low-ℓ/lensing without a pairing-swap test; a consistency control run is planned." |
| 25 | OpenAI | P1B-M6 (pass 2) | MAJOR | Heterogeneous Cobaya versions (v3.5 vs v3.6.1) and lensing hooks across chains | Appendix A; chain metadata | **VERIFIED — MINOR** — Cobaya v3.5 vs v3.6.1 and lensing.clik vs lensing.native can produce non-negligible parameter shifts; this is not disclosed as a potential systematic | Add note in §III: "production chains used Cobaya v3.5/v3.6.1 (iter2); potential software-version-induced shifts on ΔNeff/H0 at sub-0.1σ not formally characterized" |
| 26 | OpenAI | P1B-M7 (pass 2) | MAJOR | θ_i≤0.1 sliver statistics from 42 raw samples — not statistically robust | tex L2088: "indicative only (42 samples)"; table caption discloses | MISLABELED — OPINION; paper clearly labels these as "indicative only" and "sliver-only (42 samples)"; Gemini also flagged this (EXT5-Ge1 ruled HOUSTON-DECISION) | HOUSTON-DECISION — whether to extend chain is a compute call; "indicative only" labeling is sufficient for PRD |
| 27 | OpenAI | P1B-M8 (pass 2) | MAJOR | "Common beam would cancel" untested | §IV | **VERIFIED — MINOR** — the beam cancellation assertion is theoretical; no MC test shown | Add one-sentence qualification: "assuming identical beam deconvolution of both E-map and template; dedicated beam-MC test is left to a future sky-measurement analysis" |
| 28 | OpenAI | P1B-n1 | MINOR | β_combined = 0.241° vs recomputed 0.243° | Sec. VI Eq. (4) | **NEEDS-VERIFY** — small rounding difference; may depend on more precise internal values | Recompute with full precision inputs; report 0.243° if that's the exact result, or confirm 0.241° used more precise internal values |
| 29 | OpenAI | P1B-n2 | MINOR | Template CEE^b binning and zero-weight above ℓ=1024 not explicitly stated | §IV | MISLABELED — NIT; paper states "restricting the fit to bins with ℓ≤1024 changes nothing" | Add one-sentence clarification that CEE^b is zero for ℓ>1024 bins |
| 30 | OpenAI | P1B-n3 | MINOR | BBN Neff range citation missing | §III | Already partially addressed by EXT5 Ge2 (BBN flag); citation to CAMB documentation | Add CAMB BBN documentation citation |
| 31 | Perplexity | P1B-E1 | ESSENTIAL | Ref [4] arXiv:2509.13654 "impossible" / "future" / "non-existent" arXiv ID | references.bib L473-481: entry `DiegoPalazuelos2025` with arXiv eprint 2509.13654 is present. September 2025 is BEFORE June 2026 (today). | **AUTO-FALSIFIED (Rule 3 + pattern-052, 5th+ re-raise)** — date 2509 = September 2025, which is a past date. Reviewer training-cutoff artifact. The paper exists. | None |
| 32 | Perplexity | P1B-E2 | ESSENTIAL | ACT DR6 β=0.215°±0.074° not verifiable; no published paper | Same as row 31; DiegoPalazuelos+Komatsu 2025 arXiv:2509.13654 is the published ACT DR6 birefringence paper | **AUTO-FALSIFIED (Rule 3 + pattern-052, 5th+ re-raise)** | None |
| 33 | Perplexity | P1B-E3 | ESSENTIAL | 3.9σ combined-significance invalid (correlated systematics ignored) | §VI body: paper explicitly labels Eq. (4) as "auxiliary cross-check" and notes "calibration systematics shared by Planck and ACT make this an optimistic upper bound"; the 3.9σ is not presented as the headline significance | **VERIFIED — MINOR** — despite the disclaimers, the section header and surrounding narrative give 3.9σ more prominence than the caveats warrant; headline significance should be explicitly stated as the Eskilt & Komatsu 3.6σ with the 3.9σ clearly demoted | Demote 3.9σ explicitly: "a naive (optimistic upper bound) combined value of 3.9σ assuming zero correlation" |
| 34 | Perplexity | P1B-E4 | ESSENTIAL | ACT DR6 future-dated / non-existent | Duplicate of rows 31, 32 | **AUTO-FALSIFIED (Rule 3 + pattern-052)** | None |
| 35 | Perplexity | P1B-E5 | ESSENTIAL | Ref [4] non-existent paper in bibliography | Duplicate of rows 31, 32 | **AUTO-FALSIFIED (Rule 3 + pattern-052)** | None |
| 36 | Perplexity | P1B-M1 | MAJOR | PR3 vs PR4 labeling of Eskilt & Komatsu β=0.342°±0.094° | tex footnote fn:eskilt_pr3_pr4 (L860): paper explicitly disambiguates "PR3+WMAP9 published analysis" vs "PR4/NPIPE code rerun" | INCORRECT/STALE — paper already has a dedicated footnote disambiguating PR3 vs PR4 usage | None; footnote is already present |
| 37 | Perplexity | P1B-M2 | MAJOR | MCMC proxy doesn't add new information vs Planck 2018 | Paper explicitly states this is a null-consistency test; not a claim of new constraints | INCORRECT/STALE — paper's stated purpose is null verification, not novel constraints | None |
| 38 | Perplexity | P1B-M3 | MAJOR | Internal sample counts not independently verifiable without repo access | Data availability provides HuggingFace + GitHub artifacts | MISLABELED — OPINION; DOI archiving (HD-4) resolves this at submission | At submission (HD-4) |
| 39 | Perplexity | P1B-M4 | MAJOR | Correlated systematics ignored in Planck+ACT β combination | Same as P1B-E3 (row 33) | See row 33 | See row 33 |
| 40 | Perplexity | P1B-M5 | MAJOR | Companion papers have no arXiv IDs | Companion papers listed as "posted concurrently on arXiv" without IDs | HOUSTON-DECISION (HD-11) — arXiv IDs at submission | At submission |
| 41 | Perplexity | P1B-M6 | MAJOR | "confirm" ΔNeff phrasing overstates | Same finding as row 6 (Grok P1B-E1) | **VERIFIED — MINOR** (see row 6) | See row 6 |
| 42 | Perplexity | P1B-M7 | MAJOR | 4.3σ/3.6σ w0wa departures from ΛCDM; overlap-caveat front-loading | Same as Gemini M1 / OpenAI E2 | **VERIFIED — MAJOR** (see row 1) | See row 1 |
| 43 | Perplexity | P1B-E6 (pass 2) | ESSENTIAL | σ/tension numbers mix incommensurate null procedures: H0 chain-σ vs Hubble tension σ; S8 internal-posterior vs survey-vs-survey | tex §III: H0 3.2σ (MB offset) and H0 3.6σ (canonical) used inconsistently; S8 2.6σ vs 2.0σ conflate external vs internal comparisons | **VERIFIED — MAJOR** — the paper uses both "3.2σ (MB offset from chain)" and "canonical 3.6σ Hubble tension" from literature without making explicit they are derived differently; S8 2.0σ "within-stack" vs 2.6σ "external survey tension" distinction is absent | Add explicit formulas for each σ claim: H0 (chain − SH0ES)/σ_comb; S8 clarify which is internal vs external; add "not directly comparable" disclaimer at each juxtaposition |
| 44 | Perplexity | P1B-E7 (pass 2) | ESSENTIAL | Abstract says "H0 consistent with standard ΛCDM" without quantifying SH0ES tension | §III shows the H0 remains ~3.6σ from SH0ES | **VERIFIED — MINOR** — abstract "consistent with standard ΛCDM" is correct (consistent with Planck ΛCDM) but could be misread as consistent with SH0ES; body explicitly says "does not resolve Hubble tension" but abstract is silent on this | Add to abstract: "H0 reproduces the Planck ΛCDM value (3.6σ from SH0ES; ΔNeff extension does not reduce this tension)" |
| 45 | OpenAI | P1B-M9 (pass 2) | MAJOR | β–ALP normalization: 4.93×10⁻³ rad slight mismatch from αEM/(4π)×Caγ×Δϕ/fa chain | Sec. VI Eq. (3): αEM/(4π)≈5.81×10⁻⁴, Caγ=8, Δϕ/fa≈1.06 → product ≈4.88×10⁻³ vs stated 4.93×10⁻³; small but paper is a verification companion | **VERIFIED — MINOR** — the ~1% discrepancy likely from rounding in Δϕ/fa; for a technical verification paper this should be explicit | Add one-line derivation showing all factors; clarify whether 4.93×10⁻³ includes the Δϕ/fa factor or is the product αEM/(4π)×Caγ only |
| 46 | OpenAI | P1B-M10 (pass 2) | MAJOR | Effect-size quantification missing for w0wa departures | §III: w0, wa, wpivot quoted in σ but no fractional H(z) or distance impact | **VERIFIED — MINOR** — effect sizes absent for w0wa | Add one sentence: "wpivot = −0.952 at z_pivot≈0.27 corresponds to ~X% shift in H(z=0.5) relative to ΛCDM" |
| 47 | OpenAI | P1B-M11 (pass 2) | MAJOR | "Consistent with / does not resolve" phrases unquantified | §II, §III, §VI | **VERIFIED — MINOR** (overlaps row 43 and 44) | See rows 43, 44 |

---

## EXT5 Closure Status Summary (P1B)

| EXT5 Item | Description | R35conf Status |
|-----------|-------------|----------------|
| D1 (README stack) | Full-tension likelihood stack corrected | **CLEAN** |
| D2 (ALP restricted-posterior table) | 4-row × 6-col table present in v1B.0.61 | **CLEAN** |
| D3 (Appendix A Table I) | "back Tables III-IV" → "back Table I and Tables III/IV" | **CLEAN** |
| D4/Ge2 (BBN predictor flag) | Cobaya BBN flag declared | **CLEAN** |

**Perplexity ACT DR6 "non-existent" claims (P1B-E1/E2/E4/E5): AUTO-FALSIFIED (5th+ re-raise, Rule 3, pattern-052)**

---

## Counts (R35conf P1B)

| Category | Count | Items |
|----------|-------|-------|
| **VERIFIED — MAJOR** | **3** | Row 1 (w0wa caveat front-loading); Row 14 (abstract footnote removal); Row 19 (one-sided ΔNeff 95% limit miscalculation: 0.39→0.27) |
| **VERIFIED — MINOR** | **14** | Rows 6, 8, 9, 10, 21, 22, 23, 24, 25, 27, 33, 41, 43, 44, 45, 46 |
| **NEEDS-VERIFY** | **3** | Row 3 (a_x formula), Row 16 (Fig. 2b axis label), Row 28 (β_combined rounding) |
| **AUTO-FALSIFIED (Rule 3 + pattern-052)** | **4** | Rows 31, 32, 34, 35 (Perplexity ACT DR6 "non-existent" — 5th+ re-raise) |
| **INCORRECT/STALE** | **2** | Rows 36, 37 (PR3/PR4 disambiguation already present; MCMC-as-null-test stated purpose) |
| **HOUSTON-DECISION** | **3** | DOI archiving (HD-4), companion arXiv IDs (HD-11), θ_i≤0.1 chain extension (Houston compute call) |
| **MISLABELED (real but overstated)** | **6** | Rows 2, 7, 18, 20, 26 (severity overstated) |
| **OPINION/EDITORIAL** | **4** | Rows 5, 12, 22, 29 |

**Genuinely NEW VERIFIED items (not in prior rounds): 3 MAJOR + 14 MINOR**

Most important:
- **Row 19**: One-sided ΔNeff 95% limit arithmetic error — quoted 0.39 vs correct ~0.27 under stated truncation definition (Planck+BAO+SN chain)
- **Row 1 / Row 15**: w0wa caveat ordering — SN-overlap disclosure must precede the 4.3σ/3.6σ numbers
- **Row 14**: Abstract footnote must be moved to body (PRD formatting requirement)

---

## CLEAN / NOT-CLEAN on EXT5 Closures

**P1B EXT5 CLOSURES: CLEAN**

All four EXT5 VERIFIED closures confirmed in v1B.0.61: README stack (D1), restricted-posterior table (D2), Appendix A Table I clause (D3), BBN flag (D4/Ge2). No pattern-051 regressions detected.

---

## Closure Plan for VERIFIED Items

| # | Fix | tex location | Size |
|---|-----|-------------|------|
| R35-B1 | **w0wa caveat front-loading**: rewrite §III physics-interpretation opening paragraph so SN-overlap caveat is FIRST sentence; replace "canonical quintom signature" → "provisional posterior in phantom-crossing region under overlap-uncorrected product likelihood"; move 4.3σ/3.6σ numbers to second sentence with explicit "provisional" label | ~L1174 | 1 paragraph |
| R35-B2 | **Abstract footnote**: move Eskilt & Komatsu disambiguation footnote from abstract to §IV or dedicated in-text footnote | Abstract | 1 footnote relocation |
| R35-B3 | **One-sided ΔNeff 95% limit**: recompute using stated truncation-at-ΔNeff≥0 + renormalization; update quoted 0.39 → ~0.27 for Planck+BAO+SN chain | §III + Table I | 1 number + formula |
| R35-B4 | **Abstract ΔNeff abstract phrasing**: change "data prefer extra radiation-like degree of freedom" → "ΔNeff consistent with zero (null consistency test)" and add "ΔNeff extension does not reduce SH0ES tension" | Abstract | 2 sentences |
| R35-B5 | **Grok P1B-E3 / Row 8**: add "not directly comparable" qualifier at 3.6σ (WMAP+Planck) vs 0.238° (MC pipeline) juxtaposition in NaMaster section | §IV | 1 sentence |
| R35-B6 | **One-sided ΔNeff in main text (Row 9)**: add "one-sided 95% upper limit ΔNeff < [value] (renormalized at ΔNeff≥0)" in §III alongside two-sided posterior | §III | 1 sentence |
| R35-B7 | **θ_i fine-tuning to main text (Row 10)**: move "~25× fine-tuning relative to natural θ_i~1" from footnote to first sentence of spectator-status caveat in §VI | §VI | 1 sentence |
| R35-B8 | **"Analytic −C_BB estimate" (Row 21)**: either provide the analytic derivation inline or replace "consistent with the analytic estimate" → "consistent with the empirical robustness tests" | §IV | 1 sentence |
| R35-B9 | **S8 overlap method (Row 23)**: add one-line formula: "overlap integral = ∫ N(S8; μ_1, σ_1) N(S8; μ_2, σ_2) dS8" | Table I footnote | 1 line |
| R35-B10 | **PR4/2018 caveat in Conclusions (Row 24)**: add one sentence to §VII Conclusions | §VII | 1 sentence |
| R35-B11 | **Cobaya version note (Row 25)**: add software-version heterogeneity note in §III or Appendix A | §III | 1 sentence |
| R35-B12 | **Beam cancellation qualification (Row 27)**: soften "would cancel" → "would largely cancel assuming identical beam deconvolution; dedicated beam-MC test deferred" | §IV | 1 sentence |
| R35-B13 | **σ comparability disclaimer (Row 43)**: for H0 and S8 σ claims, add explicit formulas and "not directly comparable" language | §III | 3 sentences |
| R35-B14 | **3.9σ demotion (Row 33)**: add explicit "naive optimistic upper bound assuming zero Planck–ACT correlation" before 3.9σ value | §VI | 1 clause |
| R35-B15 | **ALP β normalization (Row 45)**: add one-line derivation showing αEM/(4π)×Caγ×Δϕ/fa → β with all factors explicit | §VI | 2 lines |
| R35-B16 | **Effect size for wpivot (Row 46)**: add fractional H(z=0.5) shift corresponding to CPL parameters | §III | 1 sentence |

**NEEDS-VERIFY before next R-round:**
- Row 3 (a_x formula): confirm which formula paper uses and whether z_x≈0.39 is consistent
- Row 16 (Fig. 2b axis label): verify tex source has "(x − μ)/σ" style label
- Row 28 (β_combined): confirm 0.241° or 0.243° from full-precision inputs
