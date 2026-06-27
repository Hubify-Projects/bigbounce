# P2 R56 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R56_P2/02_full_draft.pdf` md5=592c7849 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (4869 chars)
**Wall time**: 237.1s

---

Referee report (methods/statistics), Physical Review D

I read the full 28‑page manuscript, including all figures, tables, equations, appendices, and the abstract. Below I list all methodological, statistical, and internal-consistency findings. Each item includes an ID, location, the concrete problem (with quotes where appropriate), and the required fix. Severity levels: ESSENTIAL (must fix before acceptance), MAJOR, MINOR, NIT.

ESSENTIAL FINDINGS

P2‑E1 (Eq. 9 typesetting/meaning; p. 12). Problem: Ambiguous algebra in the closed‑form Bayes factor. The text says the denominator “evaluates to an error‑function difference” and then presents
B = W/(√(2π) σeff) Φ((fmax+35/8)/σeff) − Φ((fmin+35/8)/σeff).
As written, this looks like multiplication by the CDF difference rather than division by it. From Eq. (8), B = [W N(…)] / [∫ N(…) df], and ∫ N(…) df over a finite interval equals the CDF difference; hence the correct expression is B = [W/(√(2π) σeff)] / [Φ(u2) − Φ(u1)], with explicit parentheses showing division. Required fix: Re‑typeset Eq. (9) unambiguously as B = [W/(√(2π) σeff)] / [Φ((fmax+35/8)/σeff) − Φ((fmin+35/8)/σeff)]. State explicitly that the bracketed term is in the denominator. This fixes a potential misinterpretation and aligns with the worked numeric examples (17.10, 14.36, 7.0).

P2‑E2 (Primary estimator and template weighting not fully specified; multiple places, esp. Sec. III.B pp. 8–9; Sec. IV p. 10). Problem: The paper’s headline SPHEREx significance depends critically on a “SPHEREx‑like noise weighting” yielding r ≈ 0.83–0.84, but the exact survey Fisher weight w(k1,k2,k3,z) used to compute r is not explicitly defined in the text (only described qualitatively as “SPHEREx‑like,” “LSS/SDB 1/k^2,” “CMB Fisher k^2”). Readers must not fetch the code to learn what was actually integrated. PRD requires the estimator and its weighting to be precisely pre‑declared in the Methods. Required fix: Provide an explicit mathematical definition of the Fisher weight used for (i) the SPHEREx‑like bispectrum overlap r that enters the 5.2–5.5σ headline, including all k‑ and z‑weights and triangle binning; and (ii) the LSS/SDB 1/k^2 and CMB‑Fisher k^2 comparison weights. If approximations (e.g., separable weights, redshift averaging) are used, state them. Put a compact formula in Sec. III.B with a reference to a fixed release tag of the code that implements it.

P2‑E3 (Data/code availability: missing immutable release; p. 24). Problem: “archived at Zenodo (DOI inserted at submission)” is a placeholder. There is no frozen DOI or commit hash for the exact version used to generate the numbers, contrary to PRD reproducibility standards. Required fix: Provide a working Zenodo DOI (or equivalent immutable archive) and the exact git commit hash/tag corresponding to the analyses in the manuscript. Ensure the archive contains the precise versions of all artifacts referenced by name (e.g., c9g_bf_table_recompute.py, c9i_epsilon_ratio_check.json, phase3_bispectrum_shape_overlap.json, etc.). Remove “inserted at submission” placeholders.

P2‑E4 (Numerical claim without derivation: photo‑z outliers cause only ~5% σ(fNL) degradation; Sec. IV p. 10–11). Problem: You state “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ∼5% … consistent with published photo‑z degradation estimates [26],” and sketch a fcat scaling of ~0.8% which does not obviously yield 5% after window convolution. No explicit Fisher calculation or controlled toy model for the bispectrum channel is provided. Required fix: Either (a) provide a quantitative derivation (or a small Fisher/two‑population toy model) showing the 5% number for the bispectrum with the stated SPHEREx selection and redshift binning, or (b) soften the statement to a qualitative expectation and remove the 5% numeral, replacing it with a bracketed reference to where such a calculation has been carried out (if available). As written, it is a load‑bearing scalar used in the systematic budget narrative and requires backing.

P2‑E5 (Shot‑noise treatment inconsistency; Sec. IV p. 10–11). Problem: You state that for anomaly‑selected tracers with n̄ ~ 10^−5 h^3 Mpc^−3 a naive Poisson scaling gives σ inflated by √11 ≈ 3.3× relative to CV but then say “the bispectrum‑estimator effective degradation at the squeezed‑limit modes that dominate fNL sensitivity is the more relevant ∼15–30%.” This large discrepancy is asserted without a calculation or citation and risks misleading readers. Required fix: Provide a quantitative argument or simulation (even a back‑of‑envelope integral weighting) that demonstrates why the effective degradation for the bispectrum is only 15–30% in this n̄ regime, or else remove the 15–30% figure and state clearly that a dedicated bispectrum Fisher including realistic shot noise is required.

P2‑E6 (Abstract–body alignment: endpoint labeling; p. 1 Abstract vs. Sec. III.B p. 8–9). Problem: The abstract says “bispectrum‑only 5.2–5.5σ at fNL = −35/8 (CMB Fisher to LSS noise‑weighted endpoints).” In the body you establish that rCMB = 0.876 > rLSS ≈ 0.83 and thus 5.5σ corresponds to CMB Fisher and 5.2σ to LSS/SPHEREx. The phrase “CMB Fisher to LSS endpoints” is directionally ambiguous and has been misread before. Required fix: Rephrase to “from LSS/SPHEREx noise‑weighted (5.2σ) to CMB‑Fisher (5.5σ) endpoints” in the abstract to match the ordering used later and avoid confusion.

P2‑E7 (Different null procedures juxtaposed: ensure explicit caveats wherever shown together; Fig. 2 p. 11, Table IV p. 20). Problem: You have taken care in Fig. 2 caption and Table IV to say the “naive uncorrected 6.25σ” is reference‑only. Verify that every place the 6.25σ and the template‑corrected 5.2–5.5σ appear side‑by‑side includes an explicit “not directly comparable” caveat. I found one additional juxtaposition on p. 9 (“the 16th–84th percentile range … 4.4–6.2σ … compared against the pre‑systematic 5.2–5.5σ band”) where the caveat is present but could be clearer. Required fix: Add a parenthetical “distinct null procedures; not directly comparable” at that p. 9 comparison to satisfy the journal’s requirement that such contrasts be explicitly disclaimed everywhere they appear.

MAJOR FINDINGS

P2‑M1 (Definition of “SPHEREx‑like weighting” and “scale‑dependent‑bias weighting”; Sec. III.B pp. 8–9). Problem: The list of 10 weighting schemes is mentioned, but only three named results are reported (r ≈ 0.829 SDB 1/k^2; r ≈ 0.830 “SPHEREx‑like”; r ≈ 0.876 CMB Fisher). There is no precise form for “SPHEREx‑like” and no table summarizing all schemes and cutoffs used to arrive at r = 0.84 ± 0.02. Required fix: Add a small table listing the weighting kernels used, the squeezed cutoff x3,min, and the resulting r, with one line corresponding exactly to the r employed in the headline significance. This makes the central r fully auditable.

P2‑M2 (Ambiguity in Eq. (5) bookkeeping vs. measured‑space bookkeeping; Sec. VI.C.d pp. 14–15). Problem: You describe two consistent bookkeepings (σeff = σ/r vs. shifting the mean to r fNL with σ unchanged), then say “both rescalings yield the same modest shift …” but later report slightly different numbers in different places. Required fix: Pick one bookkeeping convention to use throughout the paper for all Bayes‑factor figures (preferably the σeff = σ/r bounce‑amplitude space used in the headline BF ≈ 9–14) and add a one‑line statement in Sec. VI that all tabulated BF values follow that bookkeeping. Move the alternative to an appendix paragraph.

P2‑M3 (ϵ‑correction “≲ 0.4σ effect” in Table IV; p. 20). Problem: At 8% amplitude shift, Δ|fNL| ≈ 0.35. Propagated as Δσ = Δ|fNL| r/σ = 0.35×0.84/0.7 ≈ 0.42σ. You quote “≲ 0.4σ.” Required fix: Either tighten the upper bound to 0.42σ, or change the text to “≈ 0.4σ.” Please correct the table row accordingly.

P2‑M4 (Injection–recovery validation is not commensurate with the 3D LSS estimator; Sec. II p. 5–6 and Sec. III.B p. 9). Problem: The 200‑realization KSW‑type flat‑sky CMB‑like injection on SPHEREx noise PSDs is not the estimator SPHEREx will use and does not include a sky mask; yet the stated outcome rmeas = 0.90 ± 0.01 appears next to the LSS r ≈ 0.83–0.84 discussion. Although you state it is “a Fisher‑space test,” this placement invites over‑weighting the result. Required fix: Move the injection–recovery description to an appendix, or add a boxed disclaimer in the main text that this does not validate the SPHEREx 3D bispectrum pipeline and is shown only as a CMB‑like consistency check.

P2‑M5 (Figure/axis audit: ensure all axes have units and labels; Figs. 1–6). Problem: While the text references k in h Mpc−1 and kmin in h/Mpc, the figures as reproduced in the manuscript text are not visible in this review environment; based on captions, some axes may lack units (e.g., “Detection significance (σ)” is fine; but “σ(fNL) vs. minimum accessible wavenumber” must show kmin [h Mpc−1]). Required fix: Ensure every axis is labeled with quantity and units (e.g., kmin [h Mpc−1], fNL [dimensionless]). Add these explicitly in the figure source if missing.

MINOR FINDINGS

P2‑m1 (Abstract wording: “CMB Fisher to LSS noise‑weighted endpoints”; p. 1). See ESSENTIAL P2‑E6; if you adopt the requested rephrase, this MINOR can be ignored.

P2‑m2 (Consistency of Bayes‑factor example arithmetic; Sec. VI.C.b p. 13). You quote “denominator … is Φ(13.4) − Φ(−0.893) ≈ 1 − 0.186 = 0.814” for W=10, σ=0.7. This is correct. For clarity, add the intermediate computations (19.375/0.7 and −10.625/0.7) once so readers can replicate easily.

P2‑m3 (Equation (7) provenance; p. 10). You flag it as a “heuristic primordial‑field scaling check” and not a galaxy‑covariance derivation. Good. Add the missing factor that the result is independent of Nmodes only if one quotes the per‑mode fractional covariance; as written you already say “even before dividing by the mode count.” Consider adding one line quantifying a representative Nmodes (e.g., shell at k=0.03 h/Mpc in V=50 (Gpc/h)^3) to give a numerical δC/C ≪ 10^−3.

P2‑m4 (Squeezed‑limit cutoff insensitivity of r; p. 8). Claim “varying x3,min from 0.001 to 0.200 changes r by < 0.0002.” This is extremely tight. Add the number of triangles retained under each cutoff (to show the squeezed corner is underweighted in the LSS weights) or put a 1‑line table in the supplement.

P2‑m5 (Template mismatch r > 1; footnote 3 p. 8). The discussion is sound. Add a short sentence noting whether any of the five “benchmark‑matching” coefficient sets used in the ℓ‑space check yields r > 1 under the survey weight; this will reassure readers there is no pathologically boosted detection.

P2‑m6 (Bibliography details). Check that Planck PR4 reference [32] has the final journal pagination and that the quoted ±5.0 matches the paper’s table (you cite A&A 702 A204 (2025); verify the number). If it’s from the arXiv preprint, say so.

NITPICKS

P2‑n1 (Typos/phrasing). “CMB Fisher to LSS noise‑weighted endpoints” (see above). Also avoid “r → 1 bookkeeping” jargon in the abstract; consider “no template‑mismatch rebooking” for general readers.

P2‑n2 (Repeated long parentheticals). The paper is dense with in‑line asides. Some could move to footnotes or an appendix to improve readability (e.g., the detailed null‑space sampling discussion on p. 4–5).

P2‑n3 (Length). The manuscript reads like a thorough note plus extensive caveats. For the stated contribution (a sensitivity recast plus a bispectrum‑shape audit and Bayes‑factor wrapper), it could be tightened to ~18–20 pages by moving: (i) the null‑space sampling details and injection‑recovery to an appendix; (ii) the long QSFI caveat to a short paragraph with a reference.

Arithmetic and dimensional checks spot‑audit

- fNL = −35/8 = −4.375 (correct).
- Slow‑roll fNL ≈ (5/12)(1 − ns) with ns = 0.9649 gives 0.0146 (≈ 0.015 quoted).
- Ratio |−4.375|/0.015 ≈ 291.7 (≈ 290 quoted).
- Naive significance 4.375/0.70 = 6.25 (correct).
- Template‑corrected significance:
  - r = 0.829: 4.375×0.829/0.70 = 5.183 (≈ 5.2).
  - r = 0.876: = 5.475 (≈ 5.5).
- GR systematic σGR = 1.0: σeff = √(0.7^2 + 1^2) = 1.2207; 4.375×0.84/1.2207 = 3.01 (≈ 3.0).
- bϕ 30% case (σ = 0.9) + GR 1.0: σeff = √(0.9^2 + 1^2) = 1.345; 3.675/1.345 = 2.73 (≈ 2.7–2.8).
- bϕ 50% + GR 1.0: σeff = 1.414; 3.675/1.414 = 2.60 (≈ 2.6).
- ϵ‑correction 8%: ΔS ≈ 0.35×0.84/0.70 = 0.42σ (table should say ≈ 0.4–0.42σ).
- Bayes factor delta‑prior, broad competitor: 30/(√(2π)×0.7) = 17.1 (quoted 17.10).
- Delta‑prior, narrow competitor: 10/(1.7546×0.814) ≈ 7.00 (quoted).
- Gaussian bounce prior σtheory=1.0, broad competitor: 30/(√(2π)√(0.7^2+1^2)) = 9.81 (quoted 9.80).
- SSFSR BF with σ=0.7: exp((4.375/0.7)^2/2) ≈ 3.0×10^8 (table shows 3.5×10^8; acceptable given rounding/normalization; please check exact σ used).

Abstract‑last drift sweep

- Every abstract scalar (r range, 5.2–5.5σ, 2.6–5σ, Bayes factors 9–14 rebooked, 10–17 r→1, etc.) is traceable to the body. The only wording fix needed is the endpoint ordering (P2‑E6). The “sensitivity recast” characterization is consistent throughout.

Provenance surfaces

- Replace the Zenodo placeholder with a working DOI. Ensure artifacts named in the text exist in the archive with matching filenames and that a README lists their roles. Without this, the paper fails PRD reproducibility policy.

Standalone‑reader test

- Most definitions are given. The primary issue is the weight definitions for r (P2‑E2/P2‑M1). Once those are explicit, the methodology is reproducible without opening any companion paper.

Effect sizes

- You provide clear effect sizes (amplitude ratios, σ‑equivalents). This is adequate.

## Summary recommendation
MAJOR REVISIONS

The statistical framework and most computations are careful and largely consistent, and the main numbers check out. However, acceptance at PRD requires (i) unambiguous algebra in the closed‑form Bayes factor; (ii) precise, text‑level definition of the weighting used to compute the critical overlap r that drives the headline significance; (iii) removal or proper derivation of several load‑bearing systematic‑degradation numbers (photo‑z 5%, shot‑noise 15–30%); and (iv) a frozen, citable code/data release. Once these are addressed, and the minor textual clarifications applied, the paper will meet PRD methodological rigor standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P2‑E8 (Squeezed‑mode indexing and triangle ordering inconsistent; Secs. II.A–III.B, Fig. 1). Problem: The paper alternates between k1 as the long/squeezed mode (Eq. (2), Table I, Fig. 1: “BNL(k1,k,k) as k1/k→0”) and k3 as the long mode (Sec. III.B: “x3 ≡ k3/k1 … x3 → 0 corresponds to k3 ≪ k1 ≈ k2”). Elsewhere you enforce k1 ≤ k2 ≤ k3 on the triangle grid, which makes k1 the shortest side, not k3. These statements cannot all be true simultaneously and make the r–weighting and the “squeezed‑limit cutoff” discussion ambiguous. Required fix: Adopt a single convention throughout, e.g., define kL ≡ min{ki}, kS ≡ max{ki}, use xL ≡ kL/kS → 0 for the squeezed limit, and update Eq. (2), the Fig. 1 caption, the grid‑ordering sentence, and the x3 definition accordingly. If you keep index labels, explicitly state which index is the long mode in every place it is used.

MAJOR

P2‑M6 (GR row label in Table III is internally contradictory; p. 18). Problem: The row “Corrected (10% residual; = Ideal, verification only)” is labeled as having a 10% residual but then set equal to the zero‑residual “Ideal” line in the table body. The footnote later quantifies that a literal 10% residual would change the SSFSR Bayes factor from 3.5×10^8 to 3.1×10^8 (i.e., not equal). Required fix: Either (a) relabel the row to “Corrected (residual neglected; equals Ideal by construction)” or (b) keep “10% residual” and enter the corresponding numbers (e.g., BF vs. SSFSR ≈ 3.1×10^8 and the tuned‑competitor BF unchanged at the displayed precision). As written, the label and numbers conflict.

P2‑M7 (Units handling in M(k,z) with k quoted in h Mpc−1; Eq. (4), Sec. III.A). Problem: You state “wavenumbers k are quoted in h Mpc−1 throughout,” but Eq. (4) uses H0 without specifying unit conventions. In the standard definition, M(k,z) is dimensionless only if k and H0 are used in a consistent unit system (typically k in Mpc−1 and H0 in s−1 or Mpc−1 via c). Using k in h Mpc−1 implicitly introduces h factors unless offset elsewhere (e.g., via Ωm h^2). Required fix: Add a one‑sentence unit statement near Eq. (4) clarifying the unit system: whether k is converted to Mpc−1 internally when evaluating M, what numerical value/units are used for H0, and why M is dimensionless under your convention. This prevents silent h‑factor errors in reproductions.

MINOR

P2‑m7 (ℓ‑space Fisher overlap setup under‑specified; Sec. III.B p. 9). Problem: You report r = 0.878 ± 0.012 “stable across ℓref = 50–950” but never define the ℓ range, beam, or noise model used in that ℓ‑space Fisher check. Required fix: Add one line specifying the ℓ range integrated, Planck beam/noise used, and whether polarization enters. This keeps the CMB‑like cross‑check reproducible.

P2‑m8 (Planck–SSFSR Bayes‑factor row wording; Table III). Problem: The SSFSR column is extremely σ‑sensitive, and the footnote already clarifies the 10%‑residual example. To avoid misreads, append “(zero‑residual limit)” to the “Ideal” and “Corrected (=Ideal)” SSFSR entries.

P2‑m9 (Consistent use of hard/soft labels in text and figure). Problem: Fig. 1 and surrounding text alternate between calling k2 ≈ k3 the “hard” modes and using index‑based phrasing elsewhere. Once you fix P2‑E8, mirror that convention (kL, kS) consistently in Fig. 1 caption and Sec. II.A to prevent ambiguity.

P2‑m10 (Explicit numerical check for SSFSR BF approximation; Table III). Problem: You note the exponential σ‑sensitivity qualitatively. Add one parenthetical numeric line showing the exact formula/inputs used (e.g., BF ≈ exp[(μ/σ)^2/2] with μ = 4.375, σ = 0.700 → 3.0×10^8), and explain the small difference from 3.5×10^8 (integration limits, normalization, or rounding), to anchor readers.

P2‑m11 (Minor arithmetic annotation, Sec. VI.C.c). When quoting the σtheory = 0.5 case BF = 13.91, add the underlying numbers once (W, σeff) to match the style used elsewhere for the narrow‑prior example.

NITPICKS

P2‑n4 (Phrase tightening around Fig. 5). The caption’s “3σ threshold, 5σ threshold” should be visually present; if not, adjust the caption or add horizontal guide lines to match.

P2‑n5 (Consistent symbol for σeff). In a few places σeff is used for different combinations (e.g., σ(fNL)/r vs. √(σ^2+σGR^2)). Consider a brief sentence near Table IV explicitly defining σeff as “the effective per‑scenario denominator after all applicable rebookings and quadrature additions,” to forestall confusion.

Explanation for scope: The fresh pass focused on notation/indexing consistency, table‑label accuracy, and unit hygiene in M(k,z) (items that often slip through initial reviews). The rest of the paper’s arithmetic spot‑checks and body‑vs‑caption claims remain consistent with your earlier values and do not require additional flags beyond those already listed in the initial report.